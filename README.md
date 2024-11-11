# **Fast Fourier Transform App**

A Fast Fourier Transform (FFT) application built with Python and tkinter, allowing users to input polynomials and perform FFT-based polynomial multiplication.

## **Features**
- Input fields for entering two polynomials, with one input box per polynomial degree.
- Calculates the product of two polynomials using the Fast Fourier Transform (FFT) algorithm.
- Displays the resulting polynomial coefficients after multiplication.
- (in development...) Clear and reset options for input boxes.
- User-friendly GUI with tkinter for easy interaction.

## **Getting Started**
### Prerequisites
- **Python**: Ensure you have Python installed. The app uses tkinter, which comes bundled with Python on most platforms. To check if tkinter is installed, run:
``` 
python -m tkinter
```
- **Dependencies**: The project requires NumPy for FFT calculations.

### Installation
1. Clone the repository:  
```
git clone https://github.com/JoaoMLViegas/fast_fourier_transform_app.git  
cd fast_fourier_transform_app
```
2. Install dependencies from requirements.txt:  
``` 
pip install -r requirements.txt
```
3. Run the app:      
```
python fast_fourier_transform_app.py
```

## **Usage**
1. Input Polynomials:  
   - Enter the coefficients for each degree of the first polynomial in the provided input boxes (one box per degree).
   - Do the same for the second polynomial.
2. Perform FFT Multiplication:  
   - Click the "Multiply" button to calculate the product of the two polynomials using FFT.
3. View Results:  
   - The resulting polynomial’s coefficients are displayed on the screen, showing the product in standard polynomial form.

## **Project Structure**
fast_fourier_transform_app/  
├── fft_app.py &emsp;# Main app code with tkinter GUI  
├── fft.py &emsp;# Fast fourier transform calculations code  
├── requirements.txt &emsp;# Project dependencies  
├── README.md &emsp;# Project documentation  
└── LICENSE &emsp;# Project license  

## **Screenshots**
(To be added...) Add a screenshot of the app here to give a quick preview.

## **License**
This project is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).  
See the [LICENSE](LICENSE) file for more details.