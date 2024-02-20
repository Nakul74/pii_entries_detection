import helper

def get_response_schema(results):
    pii_entries_dict = {i:j for i,j in helper.pii_entries_dict.items() if i in list(results.keys())}
    response_schema_dict = {i:'\'VALID\' or \'INVALID\' based on pii criteria' for i,j in pii_entries_dict.items()}
    output_parser,format_instructions = helper.get_output_parser(response_schema_dict)
    return pii_entries_dict,output_parser,format_instructions


def get_chat_prompt():
    system_prompt = "You are a helpful assistant"
    system_prompt_variables = []

    human_prompt = "Your goal is to verify Personally Identifiable Information (PII) given below. The specified PII entries and their corresponding criteria are listed below.If pii entry meets the criteria then mark it as \'VALID\' else \'INVALID\'"
    human_prompt += '\n' + '###' * 30
    human_prompt += "\n<<PII entries and their corresponding criteria>>:\n{pii_entries}\n"
    human_prompt += '\n' + '###' * 30
    human_prompt += '\n{format_instructions}\n'
    human_prompt_variables = ['pii_entries','user_text','format_instructions']

    chat_prompt = helper.get_prompt_tamplate(system_prompt,system_prompt_variables,human_prompt,human_prompt_variables)
    return chat_prompt

def get_pii_entries_validation(chat_model,results):
    pii_entries_dict,output_parser,format_instructions = get_response_schema(results)
    d = {}
    d['pii_entries'] = '\n'.join([i+': '+j for i,j in pii_entries_dict.items()])
    d['format_instructions'] = format_instructions
    
    chat_prompt = get_chat_prompt()
    chain = chat_prompt | chat_model | output_parser
    results = chain.invoke(d)
    return results