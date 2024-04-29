## Project Description:

**Purpose:**
- Enhance education by aiding teachers and professors*
  
**User Interface :** Built using streamlit 

Jupyter Notebook & Modular Programming :
- This was a testing ground to try out the code and run various experiments
- Created a local package out with various files for different functions for final implementation

Overall Structure:
- Store openai api key in environment variable
- Use ChatOpenAI to create an LLM agent
- Data is user defined can be pdf, text, etc. ( MCQ only from provided data )
- Create a structured prompt template for user question
- Define LLM chain using prompt template and LLM agent
- Create prompt template for reviewing response
- Create a LLM Chain for review generation
- Define a sequential chain combining question generation and review chain
- Format output has a list of dictionaries containing mcq no., options and correct answer

Interface & Output:
  - Options to enter topic, number of questions , diffuclty level
  - Provide data source like textbook PDF, text, etc.
  - Output generates is a table with  MCQ no. , 4 options and correct answer
  - Output includes a short evaluation of quiz generated
 
Next Steps:
- Use selenium automation to create a google form using generated questions 
