from textsummerzer.config.configuration import configrationManager

from transformers import AutoTokenizer, pipeline

class predition_pipline:
    def __init__(self):
        self.config = configrationManager().get_model_evaluation_config()
    def predict(self,text):
        tokenizer=AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs={'lenght_penality':0.0,'num_beams':8,"max_length":124}
        pipe=pipeline('text-generation',model=self.config.model_path, tokenizer=tokenizer)  
        print('dialogue')
        output=pipe(text, **gen_kwargs)[0]['generated_text']
        print('\nmodel summary  ')
        print(output)
        return output               