import click
import os
import pywal

#pyds


class Builder:
    def __init__(self, src):
        self.make_with_template(src, 'source/dwm/')
        self.make_with_template(src, 'source/st/')

    def get_colors(self, src):
        return pywal.colors.get(pywal.image.get(src))['colors']
    def make_with_template(self, src, path):
        temp = open(path + 'template', 'r').read()
        file = open(path + 'config.h', 'w')
        pall = self.get_colors(src)
        keys = list(self.get_colors(src).keys())
        keys.reverse()
        for key in keys:
            temp = temp.replace(key, pall[key].lower())
        file.write(temp)
        file.close()


@click.group
def cli():
    pass

@click.command()
def install():
    os.system('bash backend/libs_install')

@click.command()
@click.argument('i')
def compile(i):
    b = Builder(i)
    os.system("bash backend/build")


cli.add_command(compile)
cli.add_command(install)

if __name__ == "__main__":
	cli()
