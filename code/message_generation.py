from openai import OpenAI
from pydantic import BaseModel
from dotenv import load_dotenv, find_dotenv

load_dotenv(".env")
client = OpenAI()
MODEL = "gpt-4o-mini"
MODEL = "gpt-4o" 
MODEL = "gpt-4o-2024-08-06"


class Output(BaseModel): 
    flash_card: str
    patient_vignette: str
    explanation: str

def generateVignette(flash_cards):

    prompt = f"""
Always use the language of the chosen flash card when creating your answers. eg: german->german

You will receive a list of medical flashcards below. Please follow these instructions for each selected card:

1. **Select and Return**: Choose one flashcard and return its content from front AND back as provided, remove images.
    - front
    - back

2. **Create a Patient Vignette**:
   - Develop a short clinical vignette based on the selected flashcard.
   - Conclude the vignette with a related clinical question.
   - *Important*: Do not reveal the diagnosis within the vignette.

3. **Diagnosis and Learning Points**:
  - for this Use Markdown!
   - Provide a brief explanation of the diagnosis and answer the clinical question.
   - Emphasize three key learning points related to the diagnosis and number them. 
     Learning Points
     1. 
     2. 
     3. 
     
     Highlight key terms and facts, such as key symptoms, key diagnostic results, medications, etc

Below are the flashcards provided:
{flash_cards}

"""

    output = client.beta.chat.completions.parse(
        model=MODEL,
        messages =  [ {"role": "system", "content": "You are a generating patient vignettes."},
                {"role": "user", "content": prompt}],
                response_format=Output,
    )

    vignette =  output.choices[0].message.parsed.patient_vignette
    explanation = output.choices[0].message.parsed.explanation
    flash_card = output.choices[0].message.parsed.flash_card
    return {"vignette":vignette, "explanation":explanation, 
    "flash_card":flash_card
    }


