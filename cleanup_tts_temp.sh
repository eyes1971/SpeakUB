





#!/bin/bash
# cleanup_tts_temp.sh
# Cleanup script for orphaned TTS temporary files
# This is a safety net for files that weren't cleaned up properly by the application

# Default age threshold (in days)
AGE_DAYS=${1:-1}

echo "Cleaning up TTS temporary files older than $AGE_DAYS day(s)..."

# Find and remove old temporary MP3 files
# Pattern matches files created by tempfile.NamedTemporaryFile with suffix=".mp3"
CLEANED_COUNT=$(find /tmp -name "tmp*.mp3" -mtime +$((AGE_DAYS-1)) -type f -delete -print | wc -l)

if [ "$CLEANED_COUNT" -gt 0 ]; then
    echo "Cleaned up $CLEANED_COUNT orphaned TTS temporary file(s)"
else
    echo "No orphaned TTS temporary files found"
fi

echo "Cleanup completed."
