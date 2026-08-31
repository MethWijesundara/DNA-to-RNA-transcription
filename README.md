# DNA → RNA Transcription
<img width="828" height="745" alt="image" src="https://github.com/user-attachments/assets/376f80d7-d6b3-447f-bb50-01a32c5ea911" />

A small Python program I wrote while studying a little Biology. 

The program takes a DNA sequence (like AGCT) and generates the corresponding RNA sequence (for AGCT, it's UCGA ) by replacing each DNA base with its complementary RNA base. 

## Concepts I understood while building this project
- A **dictionary** was used to store the complementary DNA → RNA base pairs. 
- Used string manipulation to convert any lowercase sequences to uppercase.
- Used `''.join()` and a **generator expression** to build the resulting RNA sequence. 

## Vulenrabilities
- This program can technically break if someone enters an invalid character
- Will be fixing input validation with a future update :)
