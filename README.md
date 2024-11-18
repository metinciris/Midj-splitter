# Midj-splitter

This Python tool allows you to **split multiple images into four equal parts** and save the resulting images in **WebP format** with sequential numbering (_01, _02, etc.). It features a user-friendly interface for selecting input files and output directories.

## Features
- **Batch Processing**: Supports multiple image files at once.
- **Split into 4 Parts**: Divides each image into four equal quadrants.
- **WebP Conversion**: Saves the resulting images in `.webp` format for better compression and quality.
- **Custom Naming**: Automatically names the files in `_01`, `_02`, etc., format.
- **Easy-to-Use GUI**: Select files and output folder through a graphical interface.

## Requirements
Before running the script, ensure you have the following installed:

- Python 3.6 or higher
- [Pillow](https://pillow.readthedocs.io/) for image processing

Install Pillow using pip:
```bash
pip install pillow
```

## How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/image-splitter.git
   cd image-splitter
   ```

2. Run the Python script:
   ```bash
   python image_splitter.py
   ```

3. Select the images you want to process from the file dialog.
4. Choose an output directory where the split images will be saved.
5. The script will split each image into four parts and save them in the selected folder with names like:
   ```
   originalname_01.webp
   originalname_02.webp
   originalname_03.webp
   originalname_04.webp
   ```

## Example
### Input:
An image named `example.png`:
```
+-----------------+
|        1        |
|                 |
+-----------------+
|        2        |
+-----------------+
|        3        |
|                 |
+-----------------+
|        4        |
+-----------------+
```

### Output:
Four WebP images:
- `example_01.webp`
- `example_02.webp`
- `example_03.webp`
- `example_04.webp`

## Screenshot
Below is a sample of the file selection window:

![File Selection Screenshot](https://via.placeholder.com/450)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Feel free to submit issues or pull requests if you’d like to improve the tool!

