import jinja2
import yaml

# Where's the folder with my templates
template_loader = jinja2.FileSystemLoader(searchpath="./{{cookiecutter.dir_template}}")
template_env = jinja2.Environment(loader=template_loader)

# Which file is my template
{{cookiecutter.template_file}} = "{{cookiecutter.template_file}}.tpl"
template = template_env.get_template({{cookiecutter.template_file}})

# Loading my variables, stored in a YAML file
with open("{{cookiecutter.variables_file}}.yaml", 'r') as variables_file:
    variables = yaml.safe_load(variables_file)

    outputText = ""
    # Generating the output for BundleEthernet interfaces
    for element in range(len(variables)):
        # TODO
        # outputText += template.render(var1 = "foo", var2 = "bar")
        outputText += template.render()

# Saving the output in a text file
# Content of the file gets removed every time. Then content is added.
with open("./outputs/{{cookiecutter.output_file}}.txt", "w") as output_file:
    print(outputText, file=output_file)