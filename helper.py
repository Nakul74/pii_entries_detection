from langchain_openai import ChatOpenAI
from langchain.prompts import (
    PromptTemplate,
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

def get_prompt_tamplate(system_prompt,system_prompt_variables,human_prompt,human_prompt_variables):
    system_prompt = PromptTemplate(input_variables = system_prompt_variables, template=system_prompt)
    system_message_prompt = SystemMessagePromptTemplate(prompt=system_prompt)

    human_prompt = PromptTemplate(input_variables=human_prompt_variables,template=human_prompt)
    human_message_prompt = HumanMessagePromptTemplate(prompt=human_prompt)

    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    return chat_prompt

def get_output_parser(d):
    response_schemas = []
    for name,descp in d.items():
        response_schemas.append(ResponseSchema(name=name, description=descp))
    
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
    format_instructions = output_parser.get_format_instructions()
    
    return output_parser,format_instructions

def get_chat_model(openai_api_key,model_name,temperature,max_retries=5):
    chat_model = ChatOpenAI(model_name=model_name, openai_api_key=openai_api_key, temperature=temperature,max_retries = 5)
    return chat_model

pii_entries_dict = {
    "CREDIT_CARD": "A credit card number is between 12 to 19 digits",
    "DATE_TIME": "Absolute or relative dates or periods or times smaller than a day.",
    "EMAIL_ADDRESS": "An email address identifies an email box to which email messages are delivered",
    "IBAN_CODE": "The International Bank Account Number (IBAN) is an internationally agreed system of identifying bank accounts across national borders to facilitate the communication and processing of cross border transactions with a reduced risk of transcription errors.",
    "IP_ADDRESS": "An Internet Protocol (IP) address (either IPv4 or IPv6).",
    "NRP": "A person’s Nationality, religious or political group.",
    "LOCATION": "Name of politically or geographically defined location (cities, provinces, countries, international regions, bodies of water, mountains)",
    "PERSON": "A full person name, which can include first names, middle names or initials, and last names.",
    "PHONE_NUMBER": "A telephone number",
    "URL": "A URL (Uniform Resource Locator), unique identifier used to locate a resource on the Internet",
    "US_BANK_NUMBER": "A US bank account number is between 8 to 17 digits.",
    "US_DRIVER_LICENSE": "A US driver license according to https://ntsi.com/drivers-license-format/",
    "US_ITIN": "US Individual Taxpayer Identification Number (ITIN). Nine digits that start with a '9' and contain a '7' or '8' as the 4 digit.",
    "US_PASSPORT": "A US passport number with 9 digits.",
    "US_SSN": "A US Social Security Number (SSN) with 9 digits."
}