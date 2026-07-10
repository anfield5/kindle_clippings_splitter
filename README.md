# Kindle Clippings Splitter

A robust Python 3 utility that automatically parses the raw `My_Clippings.txt` file from your Amazon Kindle device, organizes your notes, highlights, and bookmarks by book title, and splits them into individual text files.

## Features

- **Automatic Windows/Kindle BOM Handling:** Uses `utf-8-sig` encoding to transparently strip hidden byte-order marks (`\xef\xbb\xbf`).
- **OS-Safe Filenames:** Automatically sanitizes book titles by removing forbidden characters (`\ / : * ? " < > |`) to prevent filesystem errors.
- **Clean Aggregation:** Groups scattered clippings belonging to the same book into a single text file.
- **Fail-Safe Logging:** Generates a `log.txt` if any file writing operation fails.
- **Test-Ready Fallback:** Automatically switches to `test_clippings.txt` if your real Kindle file isn't present in the workspace.

## Project Structure

```text
├── kindle_clippings_splitter.py  # Main script
├── My_Clippings.txt              # Your actual Kindle notes (ignored by git)
├── test_clippings.txt            # Large sample file for demonstration
├── log.txt                       # Error tracking log (ignored by git)
└── books/                        # Output folder containing organized text files (ignored by git)