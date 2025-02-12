# Customer Satisfaction Analysis  
This project uses sentiment analysis to classify customer satisfaction based on their responses. It utilizes the `Streamlit` library for the graphical interface and the `VADER` tool from the `NLTK` library for sentiment analysis.  

## Technologies Used  
- **Streamlit**: Framework for building interactive user interfaces for machine learning applications.  
- **NLTK (Natural Language Toolkit)**: Python library for natural language processing.  
- **VADER (Valence Aware Dictionary and sEntiment Reasoner)**: Sentiment analysis tool that classifies sentiment into positive, negative, or neutral categories.  

## Functionality  
This system allows the user to enter a text (feedback) about the service provided. The text is then analyzed to determine whether the feedback is:  
- **Neutral**  
- **Negative**  
- **Positive**  

## How to Use  
1. **Install the dependencies**:  
   Make sure to install the necessary libraries in your environment:  
   `pip install streamlit nltk`  

2. **Download NLTK data**:  
   The code uses the VADER lexicon for sentiment analysis, so you need to ensure that NLTK has the appropriate lexicon:  
   `import nltk  
   nltk.download('vader_lexicon')`  

3. **Run the code**:  
   You can run the Streamlit application with the following command:  
   `streamlit run your_file_name.py`  

4. **Interact with the system**:  
   - When the application is running, the user will see an input field where they can provide feedback about the service.  
   - The system will classify the feedback as "Positive", "Negative", or "Neutral" based on VADER sentiment analysis.  

## Example Output  
- If the user enters the feedback:  
  `"The service was great!"`, the response will be classified as **"Good review! 😃"**.  
- If the user enters:  
  `"I didn't like the service."`, the response will be classified as **"Bad review! 😟"**.  
- If the feedback is neutral, such as:  
  `"The service was okay."`, it will be classified as **"Neutral review 😐"**.  

## Dependencies  
- `streamlit`  
- `nltk`  

## Contributions  
If you would like to contribute to this project, please fork the repository, make your changes, and submit a pull request.  

## License  
This project is licensed under the MIT License.

