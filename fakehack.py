#!/usr/bin/env python3
import click
from time import sleep
from socket import getaddrinfo
import random
import sys
import itertools

@click.command()
@click.argument("user")
@click.argument("host")
@click.pass_context
def cli(ctx, user, host):
    click.clear()
    ctx.obj = dict(user=user, host=host)
    args = []
    cmd = ""
    while True:
        line = inputline(ctx.obj["user"], ctx.obj["host"], "~")
        cmd, *args = line.split()
        cmd_o = shell.get_command(ctx, cmd)
        if cmd_o == None:
            click.echo("%s: command not found" % cmd)
        else:
            try:
                #cmd_o.main(args, cmd, standalone_mode=False)
                cmd_ctx = cmd_o.make_context(cmd, args)
                cmd_ctx.obj = ctx.obj
                cmd_o.invoke(cmd_ctx)
            except click.ClickException as e:
                e.show()
            

def inputline(user, host, cwd):
    userstyle = ""
    atchar = click.style("@", fg="yellow", bold=True)
    hoststyle = click.style(host, fg="green", bold=True)
    cwdstyle = click.style(cwd, fg="blue", bold=True)
    promptchar = ""
    
    if user == "root":
        userstyle = click.style(user, fg="red", bold=True)
        promptchar = click.style("#", fg="red", bold=True)
    else:
        userstyle = click.style(user, fg="green", bold=True)
        promptchar = click.style("$", fg="blue", bold=True)
    
    promptline = userstyle + atchar + hoststyle + " " + cwdstyle + \
                 " " + promptchar
    
    return click.prompt(promptline, prompt_suffix=' ')

@click.group()
def shell():
    pass

@shell.command()
@click.argument("code", default=0)
def exit(code):
    sys.exit(code)

@shell.command()
@click.argument("host")
@click.pass_context
def h4xx0rz(ctx, host):
    ip = get_ip(host)
    click.secho("Hacking %s (%s)" % (host, ip),
                fg="white", bg="red", bold=True)
    
    with click.progressbar(range(7),
                           label="Connecting to proxies...",
                           show_pos=True) as bar:
        for proxy in bar:
            sleep(random.uniform(0.3,0.7))
    click.secho("=> CONNECTED", fg="green", bold=True)
    click.echo("")
    
    with click.progressbar(range(2**16),
                           label="Stealth-probing ports...",
                           show_pos=True) as bar:
        for port in bar:
            pass
    click.secho("=> Found ", fg="green", bold=True, nl=False)
    click.secho(str(random.randint(2, 16)), fg="yellow", bold=True, nl=False)
    click.secho(" open ports", fg="green", bold=True)
    click.echo("")
    
    click.secho("Scanning for vulnerabilities... ", bold=True, nl=False)
    show_spinner(15, bold=True)
    click.echo("")
    gibe_lines_pls_scrollerino(11)
    click.secho(" - Attempting stack smash... ", nl=False)
    show_spinner(15, work=memdump)
    click.secho("=> Stack pwned", bold=True, fg="green")
    click.echo("")
    
    click.echo("Injecting shell code", nl=False)
    for _ in range(6):
        click.echo(".", nl=False)
        sleep(0.5)
    click.secho(" SUCCESS", fg="green", bold=True)
    click.echo("")
    
    click.echo("Connecting to remote shell at %s:%d... " %
               (ip, random.randint(8000, 2**16 - 1)), nl=False)
    show_spinner(random.randint(8, 17))
    click.secho("=> CONNECTED", bold=True, fg="green")
    click.echo("")
    
    click.secho("Beginning the pursuit for root", bold=True, fg="yellow")
    click.secho("Attempting kernel exploits...", bold=True)
    sleep(1)
    click.echo(" - Reducing ASLR entropy... ", nl=False)
    show_spinner(3)
    click.echo(" - Spraying heap... ", nl=False)
    show_spinner(10)
    click.echo("")
    click.secho("***********************", fg="green", bold=True)
    click.secho("* ", fg="green", bold=True, nl=False)
    click.secho("w00t w00t g0t r00t!", fg="green", bold=True, blink=True, nl=False)
    click.secho(" *", fg="green", bold=True)
    click.secho("***********************", fg="green", bold=True)
    click.echo("")
    
    ctx.obj["user"] = "root"
    ctx.obj["host"] = host
    
    with click.progressbar(range(100), label="Installing backdoors...") as bd:
        for b in bd:
            sleep(0.025)
    
    click.echo("")
    click.secho(pwnedsign, fg="red")
    click.echo("")

def get_ip(host):
    return getaddrinfo(host, None)[0][-1][0]

def show_spinner(spins, work=None, interval=0.4, **style):
    spinner = itertools.cycle(['─', '\\', '|', '/'])
    sys.stdout.write('\x1b[?25l')
    for i in range(spins):
        done = (i == spins - 1)
        sys.stdout.write(click.style(next(spinner), **style))
        sys.stdout.write('\b')
        sys.stdout.flush()
        if done:
            sys.stdout.write(' ')
        
        if work:
            sys.stdout.write('\x1b[s') # Save cursor
            sys.stdout.write('\n\n')
            work(last=done)
            if not done:
                sys.stdout.write('\x1b[u') # Restore cursor
        
        sleep(interval)
        
    sys.stdout.write('\x1b[?25h\n')

def gibe_lines_pls_scrollerino(num):
    sys.stdout.write("\n" * num)
    sys.stdout.write("\x1b[%dA" % num)
    sys.stdout.flush()

# 8 * 60
# I need to seriously re-think this
def memdump(last):
    for y in range(8):
        sys.stdout.write("%08x" % (y * 16))
        for words in range(4):
            sys.stdout.write("  ")
            if last and y == 7 and words == 3:
                click.secho("DE AD BE EF", bold=True, nl=False)
            else:
                pass
                sys.stdout.write("%02X %02X %02X %02X" % 
                                 tuple(random.sample(range(256), 4)))
        
        #sys.stdout.write("\x1b[1E")
        sys.stdout.write("\n")
    
# You might not believe it but this here is actually syntactically
# correct, so please don't panic if your highlighting is broken.
pwnedsign = r"""
                                                             ..       
                x=~                                        dF         
 .d``          88x.   .e.   .e.     u.    u.              '88bu.      
 @8Ne.   .u   '8888X.x888:.x888   x@88k u@88c.      .u    '*88888bu   
 %8888:u@88N   `8888  888X '888k ^"8888""8888"   ud8888.    ^"*8888N  
  `888I  888.   X888  888X  888X   8888  888R  :888'8888.  beWE "888L 
   888I  888I   X888  888X  888X   8888  888R  d888 '88%"  888E  888E 
   888I  888I   X888  888X  888X   8888  888R  8888.+"     888E  888E 
 uW888L  888'  .X888  888X. 888~   8888  888R  8888L       888E  888F 
'*88888Nu88P   `%88%``"*888Y"     "*88*" 8888" '8888c. .+ .888N..888  
~ '88888F`       `~     `"          ""   'Y"    "88888%    `"888*""   
   888 ^                                          "YP'        ""      
   *8E                                                                
   '8>                                                                
    "                                                                 

"""


if __name__ == '__main__':
    cli()