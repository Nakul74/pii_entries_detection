import helper

def get_response_schema():
    response_schema_dict = helper.pii_entries_dict
    output_parser,format_instructions = helper.get_output_parser(response_schema_dict)
    return output_parser,format_instructions

def get_chat_prompt():
    system_prompt = "You are a helpful assistant"
    system_prompt_variables = []

    human_prompt = "Your goal is to identify Personally Identifiable Information (PII) in the text provided by the user. The specified PII entries and their corresponding criteria are listed below. If no PII entry is found, label it as \'Not Found\'."
    human_prompt += '\n' + '###' * 30
    human_prompt += '\n<<User text>>:\n{user_text}\n'
    human_prompt += '\n' + '###' * 30
    human_prompt += "\n<<PII entries and their corresponding criteria>>:\n{pii_entries}\n"
    human_prompt += '\n' + '###' * 30
    human_prompt += '\n{format_instructions}\n'
    human_prompt_variables = ['pii_entries','user_text','format_instructions']
    chat_prompt = helper.get_prompt_tamplate(system_prompt,system_prompt_variables,human_prompt,human_prompt_variables)
    return chat_prompt

def get_pii_entries(chat_model,user_text):
    d = {}
    d['pii_entries'] = '\n'.join([i+': '+j for i,j in helper.pii_entries_dict.items()])
    d['user_text'] = user_text
    
    output_parser,format_instructions = get_response_schema()
    d['format_instructions'] = format_instructions
    
    chat_prompt = get_chat_prompt()
    chain = chat_prompt | chat_model | output_parser
    results = chain.invoke(d)
    results = {i:j for i,j in results.items() if j.lower() != 'not found'}
    return results