# DNA → RNA Transcription
## Preview
<img width="693" height="881" alt="image" src="https://github.com/user-attachments/assets/b56b83ff-ad1c-4d76-899e-3b4e598aa2bd" />

## About this project
A small Python program I wrote while studying a little Biology. 

The program takes a DNA sequence (like AGCT) and generates the corresponding RNA sequence (for AGCT, it's UCGA ) by replacing each DNA base with its complementary RNA base. 

## Concepts I understood while building this project
- A **dictionary** was used to store the complementary DNA → RNA base pairs. 
- Used string manipulation to convert any lowercase sequences to uppercase.
- Used `''.join()` and a **generator expression** to build the resulting RNA sequence. 

## vulnerabilities
- This program can technically break if someone enters an invalid character
- Will be fixing input validation with a future update :)
