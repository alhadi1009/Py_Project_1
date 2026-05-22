# Animated Smart PDF System

#### Video Demo: <Video Provide soon...>

---

##  Description

The **Animated Smart PDF System** is a Python-based automation project that generates different types of documents such as certificates,and ID cards. It is designed to simplify and automate the process of creating structured PDF documents with dynamic user input.

This project was built using Python and combines multiple functionalities such as PDF generation, image processing, CSV handling, QR code generation, and file management. The system provides a menu-driven interface where users can select different options and generate outputs based on their input.

---

##  Features

The system includes the following main features:

1. **PDF Certificate Generator**
   - Generates a professional certificate using user details such as name, course, and author/signature.
   - Uses custom fonts and background images for a stylish design.

2. **ID Card Generator**
   - Creates ID cards for multiple students.
   - Handles multiple inputs and generates a combined PDF file.

3. **QR Code & File Handling**
   - Generates text-based data files.
   - Supports QR-related data processing (via helper modules).

4. **Image Processing**
   - Cleans and resizes images for ID card generation.
   - Automatically manages image files after processing.

5. **CSV Handling**
   - Stores and manages student data using CSV files.
   - Automatically cleans temporary data after execution.

---

##  Project Structure

The project is divided into multiple Python modules:

- `project.py` → Main entry point of the application (menu system and control logic)
- `PDFGenerator.py` → Handles certificate generation using FPDF
- `FileGenerator.py` → Handles student data input and file creation
- `QRGenerator.py` → Manages QR/text file generation
- `IDCardGenerator.py` → Creates ID card layout and PDF output
- `CSVClean.py` → Cleans CSV files after processing
- `ImageClean.py` → Handles image cleanup and resizing

---

##  How It Works

1. The program starts from `project.py`.
2. A menu is displayed with available features.
3. The user selects an option:
   - PDF generation
   - ID card generation
   - Exit system
4. Based on user input, different modules are called.
5. The system processes input data and generates:
   - PDFs
   - Images
   - CSV records
6. Temporary files are automatically cleaned after execution.

---

##  Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
