import yaml
from crewai import Agent, Task, Crew, LLM

class MbtiLoopCrew:
    def __init__(self):
        with open('agents.yaml', 'r') as f:
            self.agents_config = yaml.safe_load(f)
        with open('tasks.yaml', 'r') as f:
            self.tasks_config = yaml.safe_load(f)
        

        self.ollama_llm = LLM(
            model="ollama/llama3.2:1b", 
            base_url="http://localhost:11434",
            temperature=0.1 # Bajo para respuestas mas conservadoras/deterministas
        )

    def run(self, mbti_type):
        listador = Agent(config=self.agents_config['listador_regalos'], llm=self.ollama_llm)
        selector = Agent(config=self.agents_config['selector_regalos'], llm=self.ollama_llm)

        t1 = Task(config=self.tasks_config['lluvia_ideas_task'], agent=listador)
        t2 = Task(config=self.tasks_config['critica_task'], agent=selector)
        t3 = Task(
            config=self.tasks_config['refinamiento_task'], 
            agent=listador,
            output_file='regalos_finales.md'
        )

        crew = Crew(
            agents=[listador, selector],
            tasks=[t1, t2, t3],
            verbose=True
        )
        return crew.kickoff(inputs={'mbti': mbti_type})
