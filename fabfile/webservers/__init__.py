from fabric.api import run, sudo, cd, env, task
from fabric.colors import green

from ..literals import WEB_APACHE
import apache


@task
def install_site():
    """
    Install Mayan EDMS site in the webserver configuration files
    """
    
    print(green('Adding Mayan EDMS\'s site files to: %s' % env.webserver_name, bold=True))

    if env.webserver == WEB_APACHE:
        apache.install_site()


@task
def remove_site():
    """
    Install Mayan EDMS's site file from the webserver's configuration
    """    
    print(green('Removing Mayan EDMS\'s site file from %s configuration' % env.webserver_name, bold=True))

    if env.webserver == WEB_APACHE:
        apache.remove_site()


@task    
def restart():
    """
    Restart the webserver
    """    
    print(green('Restarting the web server: %s' % env.webserver_name, bold=True))

    if env.webserver == WEB_APACHE:
        apache.restart()


@task
def reload():
    """
    Reload webserver configuration files
    """    
    print(green('Reloading the web server configuration files', bold=True))

    if env.webserver == WEB_APACHE:
        apache.reload()
