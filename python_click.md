pip install click

ex1:
```python
import click
@click.command()
@click.option('--count', type=int, default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)
if __name__ == '__main__':
    hello()
```
    
python hello.py (-count=3 --name=Ethan)

ex2:
```python
import click
@click.command()
@click.option('--gender', type=click.Choice(['man', 'woman']))    # 限定值
def choose(gender):
    click.echo('gender: %s' % gender)
if __name__ == '__main__':
    choose()
```

ex3:
设置固定长度的参数值  
```python
@click.option('--center', nargs=2, type=float, help='center of the circle')
```

ex4:
```python
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
or
@click.password_option()
```

ex5:
```python  
import click
def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 1.0')
    ctx.exit()
@click.command()
@click.option('--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
@click.option('--name', default='Ethan', help='name')
def hello(name):
    click.echo('Hello %s!' % name)
if __name__ == '__main__':
    hello()
```
    
is_eager=True 表明该命令行选项优先级高于其他选项；
expose_value=False 表示如果没有输入该命令行选项，会执行既定的命令行流程；
callback 指定了输入该命令行选项时，要跳转执行的函数；

ex6:
```python 
import click
@click.command()
@click.argument('coordinates')
def show(coordinates):
    click.echo('coordinates: %s' % coordinates)
if __name__ == '__main__':
    show()
```

ex7:    
```python 
import click
@click.command()
@click.argument('x')
@click.argument('y')
@click.argument('z')
def show(x, y, z):
    click.echo('x: %s, y: %s, z:%s' % (x, y, z))
if __name__ == '__main__':
    show()    
```    

ex8:    
```python
@click.argument('src', nargs=-1)
```    

ex9:    
```python
pip install colorama
import click
@click.command()
@click.option('--name', help='The person to greet.')
def hello(name):
    click.secho('Hello %s!' % name, fg='red', underline=True)
    click.secho('Hello %s!' % name, fg='yellow', bg='black')
if __name__ == '__main__':
    hello()
```  

fg 表示前景颜色（即字体颜色），可选值有：BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE 等；
bg 表示背景颜色，可选值有：BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE 等；
underline 表示下划线，可选的样式还有：dim=True，bold=True 等；    

