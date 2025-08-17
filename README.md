# Comparison Crew

Welcome to the Comparison Crew project, powered by [CrewAI](https://crewai.com/). This project is not just a template — its main objective is to evaluate and compare agentic AI platforms, specifically CrewAI vs Flowise, by leveraging CrewAI’s own multi-agent framework.

A set of specialized agents is orchestrated to research, analyze, and debate the strengths and weaknesses of both platforms. The crew collaborates to determine which is better suited for building scalable agentic AI solutions.

## Our Goal

Our goal is two-fold:

- Showcase CrewAI’s ability to run a structured, agent-driven investigation.
- Produce a clear comparison between CrewAI and Flowise — based on usability, flexibility, scalability, and real-world application potential.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [UV](https://github.com/astral-sh/uv) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:

```bash
crewai install
```

## Configuration

- Add your `OPENAI_API_KEY` into the `.env` file.
- Modify `src/comparison/config/agents.yaml` to define your agents.
- Modify `src/comparison/config/tasks.yaml` to define your tasks.
- Modify `src/comparison/crew.py` to add your own logic, tools, and specific args.
- Modify `src/comparison/main.py` to add custom inputs for your agents and tasks.

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
crewai run
```

This command initializes the Comparison Crew, assembling the agents and assigning them tasks as defined in your configuration.

Unmodified, this example will create a `report.md` file in the root folder containing the outcome of the CrewAI vs Flowise research.

## Understanding Your Crew

The Comparison Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives.

- The `config/agents.yaml` file outlines the capabilities and configurations of each agent.
- The tasks are structured to simulate debates, research, and reporting, ensuring a balanced comparison.

## Outcome

By the end of execution, the project generates:

- A structured comparison report (e.g., `report.md`) on CrewAI vs Flowise.
- Insights into agent-driven research, showcasing how CrewAI itself can manage complex evaluation tasks.
- A blueprint for adapting this methodology to compare other tools or frameworks.

## Support

For support, questions, or feedback regarding the Comparison Crew or CrewAI:

- Visit our [documentation](https://docs.crewai.com/)
- Reach out to us through our [GitHub repository](https://github.com/crewAI)
- Join our [Discord](https://discord.com/invite/crewAI)
- Chat with our docs

Let’s create wonders together with the power and simplicity of CrewAI 🚀

Made by Vishvvesh Nagappan
