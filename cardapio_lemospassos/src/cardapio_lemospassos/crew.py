from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from cardapio_lemospassos.tools.custom_tool import ler_regras_edital_principal, ler_regras_edital_opcao, ler_pratos_proteina_principal, ler_pratos_proteina_opcao

from pydantic import BaseModel, Field

class Pratos(BaseModel):
    pratos: str = Field(..., description="lista com os 30 dias de pratos com Dia, nome do prato, Custo,percent. de consumo e valor total")

class StatusValidacao(BaseModel):
    status: str = Field(..., description="APROVADO ou REPROVADO")
    feedback: str = Field(..., description="Feedback da validação caso seja negativa")

# class PratosPrincipais(BaseModel):
#     pratos: str = Field(..., description="lista com os 30 dias de pratos com Dia, nome do prato, Custo,percent. de consumo e valor total")
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class CardapioLemospassos_principal():
    """CardapioLemospassos crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def montador_proteina_principal(self) -> Agent:
        return Agent(
            config=self.agents_config['montador_proteina_principal'],
            tools=[ler_regras_edital_principal, ler_pratos_proteina_principal],
            verbose=True
        )

    # @agent
    # def validador_montador_proteina_principal(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['validador_montador_proteina_principal'],
    #         tools=[ler_cardapios_disponiveis],
    #         verbose=True,
    #         allow_delegation=True
    #     )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def montar_proteina_principal_task(self) -> Task:
        return Task(
            config=self.tasks_config['montar_proteina_principal_task'],
            agent=self.montador_proteina_principal(),
            output_pydantic=Pratos
        )

    # @task
    # def validar_montagem_proteina_principal_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['validar_montagem_proteina_principal_task'],
    #         agent=self.validador_montador_proteina_principal()
    #     )

    @crew
    def crew(self) -> Crew:
        """Creates the CardapioLemospassos crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            # manager_agent=Agent(
            #     config=self.agents_config['supervisor'],
            #     verbose=True,
            #     allow_delegation=True
            # ),
            verbose=True,
            memory=True,
            # planning=True,
            # planning_llm="o1-mini"
        # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )


@CrewBase
class CardapioLemospassos_validacao_principal():
    """CardapioLemospassos crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools

    @agent
    def validador_montador_proteina_principal(self) -> Agent:
        return Agent(
            config=self.agents_config['validador_montador_proteina_principal'],
            tools=[ler_regras_edital_principal],
            verbose=True,
            allow_delegation=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def validar_montagem_proteina_principal_task(self) -> Task:
        return Task(
            config=self.tasks_config['validar_montagem_proteina_principal_task'],
            agent=self.validador_montador_proteina_principal(),
            output_pydantic=StatusValidacao
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CardapioLemospassos crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            # manager_agent=Agent(
            #     config=self.agents_config['supervisor'],
            #     verbose=True,
            #     allow_delegation=True
            # ),
            verbose=True,
            memory=True,
            # planning=True,
            # planning_llm="o1-mini"
        # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )


@CrewBase
class CardapioLemospassos_opcao():
    """CardapioLemospassos crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def montador_proteina_opcao(self) -> Agent:
        return Agent(
            config=self.agents_config['montador_proteina_opcao'],
            tools=[ler_regras_edital_opcao,ler_pratos_proteina_opcao],
            verbose=True,
        )

    # @agent
    # def validador_montador_proteina_opcao(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['validador_montador_proteina_opcao'],
    #         tools=[ler_cardapios_disponiveis_opcao],
    #         verbose=True,
    #         allow_delegation=True
    #     )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def montar_proteina_opcao_task(self) -> Task:
        return Task(
            config=self.tasks_config['montar_proteina_opcao_task'],
            agent=self.montador_proteina_opcao(),
            output_pydantic=Pratos
        )


    @crew
    def crew(self) -> Crew:
        """Creates the CardapioLemospassos crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            
            verbose=True,
            memory=True,
            # planning=True,
            # planning_llm="o1-mini"
        # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )


@CrewBase
class CardapioLemospassos_opcao_validador():
    """CardapioLemospassos crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools

    @agent
    def validador_montador_proteina_opcao(self) -> Agent:
        return Agent(
            config=self.agents_config['validador_montador_proteina_opcao'],
            tools=[ler_regras_edital_opcao, ler_pratos_proteina_principal, ler_pratos_proteina_opcao],
            verbose=True,
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
        
    @task
    def validar_montagem_proteina_opcao_task(self) -> Task:
        return Task(
            config=self.tasks_config['validar_montagem_proteina_opcao_task'],
            agent=self.validador_montador_proteina_opcao(),
            output_pydantic=StatusValidacao
        )


    @crew
    def crew(self) -> Crew:
        """Creates the CardapioLemospassos crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            memory=True,
            # planning=True,
            # planning_llm="o1-mini"
        # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )


@CrewBase
class CardapioLemospassos_compiler():
    """CardapioLemospassos crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def compilador_geral_cardapios(self) -> Agent:
        return Agent(
            config=self.agents_config['compilador_geral_cardapios'],
            verbose=True,
            allow_delegation=True
        )

    @task
    def compilador_cardapio_task(self) -> Task:
        return Task(
            config=self.tasks_config['compilador_cardapio_task'],
            agent=self.compilador_geral_cardapios()
        )


    @crew
    def crew(self) -> Crew:
        """Creates the CardapioLemospassos crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            
            verbose=True,
            memory=True,
            # planning=True,
            # planning_llm="o1-mini"
        # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )


   
class CardapioLemospassos():
    def __init__(self, idea):
        self.idea = idea
        
    def run(self):
        cardapio_principal= self.runPratoPrincipal(self.idea, "Ainda não validado, crie o cardápio principal", "Ainda não gerado")
        print(cardapio_principal)
        validacao_cardapio_Principal = self.runValidacaoPratoPrincipal(cardapio_principal)
        print(validacao_cardapio_Principal)
        
        while 'REPROVADO' in validacao_cardapio_Principal :
            cardapio_principal = self.runPratoPrincipal(self.idea, validacao_cardapio_Principal, cardapio_principal)
            print("--------------- REVALIDADO ---------------")
            print(cardapio_principal)
            print("--------------- REVALIDADO ---------------")
            validacao_cardapio_Principal = self.runValidacaoPratoPrincipal(cardapio_principal)
            print(validacao_cardapio_Principal)
        
        cardapio_opcao = self.runPratoOpcao(cardapio_principal, "Ainda não validado, crie o cardápio de opção", "Ainda não gerado")
        print(cardapio_opcao)
        validacao_cardapio_opcao = self.runValidacaoPratoOpcao(cardapio_opcao)
        print(validacao_cardapio_opcao)
        
        while 'REPROVADO' in validacao_cardapio_opcao :
            cardapio_opcao = self.runPratoOpcao(cardapio_principal, validacao_cardapio_opcao, cardapio_opcao)
            print("--------------- REVALIDADO ---------------")
            print(cardapio_opcao)
            print("--------------- REVALIDADO ---------------")
            validacao_cardapio_opcao = self.runValidacaoPratoOpcao(cardapio_opcao)
            print(validacao_cardapio_opcao)
        
        cardapio_final = self.runCardapioCompilado(cardapio_principal, cardapio_opcao)
        print(cardapio_final)
            
    def runPratoPrincipal(self,idea, feedback, cardapio_anterior):
        inputs1 = {
                "topic": str(idea),
                "feedback": str(feedback),
                "cardapio_anterior": str(cardapio_anterior)
        }
        expanded_idea= CardapioLemospassos_principal().crew().kickoff(inputs=inputs1)
        return str(expanded_idea)
    
    def runValidacaoPratoPrincipal(self,cardapio_principal):
        inputs1 = {
                "cardapio_principal": str(cardapio_principal)
        }
        expanded_idea= CardapioLemospassos_validacao_principal().crew().kickoff(inputs=inputs1)
        return str(expanded_idea)
    
    def runPratoOpcao(self,cardapio_principal, feedback, cardapio_anterior):
        inputs2 = {
                "cardapio_principal": str(cardapio_principal),
                "feedback": feedback,
                "cardapio_anterior": str(cardapio_anterior)
        }
        cardapio_opcao = CardapioLemospassos_opcao().crew().kickoff(inputs=inputs2)
        return str(cardapio_opcao)
    
    def runValidacaoPratoOpcao(self, cardapio_opcao):
        inputs2 = {
                "cardapio_completo": str(cardapio_opcao)
        }
        cardapio_opcao = CardapioLemospassos_opcao_validador().crew().kickoff(inputs=inputs2)
        return str(cardapio_opcao)
    
    def runCardapioCompilado(self,cardapio_principal, cardapio_opcao):
        inputs3 = {
                "cardapio_principal": str(cardapio_principal),
                "cardapio_opcao": str(cardapio_opcao),
        }
        cardapio_compilado = CardapioLemospassos_compiler().crew().kickoff(inputs=inputs3)
        return str(cardapio_compilado)
    