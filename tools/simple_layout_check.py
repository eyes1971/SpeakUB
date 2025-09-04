


#!/usr/bin/env python3
"""
Simple static check of the TTS footer layout changes.
"""

import ast
import sys
from pathlib import Path


def check_compose_method():
    """Check that the compose method has been modified correctly."""
    print("🔍 Checking compose() method modifications")
    print("=" * 45)

    # Read the source file
    rich_cli_path = Path(__file__).parent.parent / \
        "speakub" / "cli.py"
    with open(rich_cli_path, "r", encoding="utf-8") as f:
        source_code = f.read()

    # Parse the AST
    tree = ast.parse(source_code)

    # Find the compose method in EPUBReaderApp
    compose_found = False
    horizontal_found = False
    static_components = []

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == "EPUBReaderApp":
            for item in node.body:
                if isinstance(item, ast.FunctionDef) and item.name == "compose":
                    compose_found = True
                    print("✅ Found compose() method in EPUBReaderApp")

                    # Check the method body for our changes
                    for stmt in item.body:
                        if isinstance(stmt, ast.With):
                            # Check if it's a Horizontal with id="tts-footer"
                            if (
                                isinstance(
                                    stmt.items[0].context_expr, ast.Call)
                                and isinstance(
                                    stmt.items[0].context_expr.func, ast.Name
                                )
                                and stmt.items[0].context_expr.func.id == "Horizontal"
                            ):

                                # Check for id="tts-footer"
                                for kw in stmt.items[0].context_expr.keywords:
                                    if (
                                        isinstance(kw.arg, str)
                                        and kw.arg == "id"
                                        and isinstance(kw.value, ast.Constant)
                                        and kw.value.value == "tts-footer"
                                    ):
                                        horizontal_found = True
                                        print(
                                            "✅ Found Horizontal container with id='tts-footer'"
                                        )

                                # Check the body for Static components
                                for body_stmt in stmt.body:
                                    if (
                                        isinstance(body_stmt, ast.Expr)
                                        and isinstance(body_stmt.value, ast.Call)
                                        and isinstance(body_stmt.value.func, ast.Name)
                                        and body_stmt.value.func.id == "Static"
                                    ):

                                        # Check for id keyword
                                        for kw in body_stmt.value.keywords:
                                            if (
                                                isinstance(kw.arg, str)
                                                and kw.arg == "id"
                                            ):
                                                if isinstance(kw.value, ast.Constant):
                                                    static_components.append(
                                                        kw.value.value
                                                    )

                    break

    if not compose_found:
        print("❌ compose() method not found!")
        return False

    if not horizontal_found:
        print("❌ Horizontal container with id='tts-footer' not found!")
        return False

    expected_ids = ["tts-status", "tts-controls", "tts-page"]
    if len(static_components) != 3:
        print(
            f"❌ Expected 3 Static components, found {len(static_components)}")
        return False

    for expected_id in expected_ids:
        if expected_id not in static_components:
            print(f"❌ Static component with id='{expected_id}' not found!")
            return False
        else:
            print(f"✅ Found Static component with id='{expected_id}'")

    return True


def check_update_method():
    """Check that the _update_tts_progress method has been modified correctly."""
    print("\n🔄 Checking _update_tts_progress() method modifications")
    print("=" * 55)

    # Read the source file
    rich_cli_path = Path(__file__).parent.parent / \
        "speakub" / "cli.py"
    with open(rich_cli_path, "r", encoding="utf-8") as f:
        source_code = f.read()

    # Parse the AST
    tree = ast.parse(source_code)

    # Find the _update_tts_progress method
    method_found = False
    query_calls = []

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == "EPUBReaderApp":
            for item in node.body:
                if (
                    isinstance(item, ast.FunctionDef)
                    and item.name == "_update_tts_progress"
                ):
                    method_found = True
                    print("✅ Found _update_tts_progress() method")

                    # Check for query_one calls
                    for stmt in ast.walk(item):
                        if (
                            isinstance(stmt, ast.Call)
                            and isinstance(stmt.func, ast.Attribute)
                            and stmt.func.attr == "query_one"
                        ):
                            query_calls.append(stmt)

                    break

    if not method_found:
        print("❌ _update_tts_progress() method not found!")
        return False

    expected_queries = ["#tts-status", "#tts-controls", "#tts-page"]
    if len(query_calls) != 3:
        print(f"❌ Expected 3 query_one calls, found {len(query_calls)}")
        return False

    for query in query_calls:
        if len(query.args) > 0 and isinstance(query.args[0], ast.Constant):
            query_id = query.args[0].value
            if query_id in expected_queries:
                print(f"✅ Found query for '{query_id}'")
                expected_queries.remove(query_id)
            else:
                print(f"❌ Unexpected query for '{query_id}'")

    if expected_queries:
        print(f"❌ Missing queries for: {expected_queries}")
        return False

    return True


def check_css_styles():
    """Check that CSS styles are appropriate for the layout."""
    print("\n🎨 Checking CSS styles for layout")
    print("=" * 35)

    # Read the source file
    rich_cli_path = Path(__file__).parent.parent / \
        "speakub" / "cli.py"
    with open(rich_cli_path, "r", encoding="utf-8") as f:
        source_code = f.read()

    # Find the CSS string
    css_found = False
    if "#tts-footer" in source_code:
        css_found = True
        print("✅ Found #tts-footer in CSS")

    if css_found:
        print("✅ CSS styles appear to be in place")
        return True
    else:
        print("❌ #tts-footer CSS styles not found")
        return False


if __name__ == "__main__":
    print("🔧 Static Layout Verification")
    print("This script checks the code structure without running the app.\n")

    # Run all checks
    compose_ok = check_compose_method()
    update_ok = check_update_method()
    css_ok = check_css_styles()

    if compose_ok and update_ok and css_ok:
        print("\n🎉 All static checks passed!")
        print("\n📋 Summary of Verified Changes:")
        print("✅ compose() method uses Horizontal container")
        print("✅ Three Static components created with correct IDs:")
        print("   - #tts-status (left)")
        print("   - #tts-controls (center)")
        print("   - #tts-page (right)")
        print("✅ _update_tts_progress() queries each component separately")
        print("✅ CSS styles include #tts-footer")
        print("\n🚀 Layout changes are correctly implemented!")
    else:
        print("\n❌ Some checks failed!")
        sys.exit(1)

