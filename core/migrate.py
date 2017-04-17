# -*- coding: utf-8 -*-
from __future__ import with_statement, absolute_import
import os
import argparse
import click
from alembic import __version__ as __alembic_version__
from alembic.config import Config as AlembicConfig
from alembic import command

alembic_version = tuple([int(v) for v in __alembic_version__.split('.')[0:3]])
current_app = None


class _MigrateConfig(object):
    def __init__(self, migrate, db, **kwargs):
        self.migrate = migrate
        self.db = db
        self.directory = migrate.directory
        self.configure_args = kwargs

    @property
    def metadata(self):
        """
        Backwards compatibility, in old releases app.extensions['migrate']
        was set to db, and env.py accessed app.extensions['migrate'].metadata
        """
        return self.db.metadata


class Config(AlembicConfig):
    def get_template_directory(self):
        package_dir = os.path.abspath(os.path.dirname(__file__))
        print package_dir
        return os.path.join(package_dir, 'templates')


class Migrate(object):
    def __init__(self, app=None, db=None, directory='migrations', **kwargs):
        self.configure_callbacks = []
        self.db = db
        self.directory = directory
        if app is not None and db is not None:
            self.init_app(app, db, directory, **kwargs)
            global current_app
            current_app = app

    def init_app(self, app, db=None, directory=None, **kwargs):
        self.db = db or self.db
        self.directory = directory or self.directory
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['migrate'] = _MigrateConfig(self, self.db, **kwargs)
        global current_app
        current_app = app

    def configure(self, f):
        self.configure_callbacks.append(f)
        return f

    def call_configure_callbacks(self, config):
        for f in self.configure_callbacks:
            config = f(config)
        return config

    def get_config(self, directory, x_arg=None, opts=None):
        if directory is None:
            directory = self.directory
        config = Config(os.path.join(directory, 'alembic.ini'))
        config.set_main_option('script_location', directory)
        if config.cmd_opts is None:
            config.cmd_opts = argparse.Namespace()
        for opt in opts or []:
            setattr(config.cmd_opts, opt, True)
        if x_arg is not None:
            if not getattr(config.cmd_opts, 'x', None):
                setattr(config.cmd_opts, 'x', [])
                if isinstance(x_arg, list) or isinstance(x_arg, tuple):
                    for x in x_arg:
                        config.cmd_opts.x.append(x)
                else:
                    config.cmd_opts.x.append(x_arg)
        return self.call_configure_callbacks(config)


def _init(directory=None, multidb=False):
    """Creates a new migration repository"""
    if directory is None:
        directory = current_app.extensions['migrate'].directory
    config = Config()
    config.set_main_option('script_location', directory)
    config.config_file_name = os.path.join(directory, 'alembic.ini')
    config = current_app.extensions['migrate']. \
        migrate.call_configure_callbacks(config)
    if multidb:
        command.init(config, directory, 'tornado-multidb')
    else:
        command.init(config, directory, 'tornado')


def _revision(directory=None, message=None, autogenerate=False, sql=False,
              head='head', splice=False, branch_label=None, version_path=None,
              rev_id=None):
    """Create a new revision file."""
    config = current_app.extensions['migrate'].migrate.get_config(directory)
    if alembic_version >= (0, 7, 0):
        command.revision(config, message, autogenerate=autogenerate, sql=sql,
                         head=head, splice=splice, branch_label=branch_label,
                         version_path=version_path, rev_id=rev_id)
    else:
        command.revision(config, message, autogenerate=autogenerate, sql=sql)


def _migrate(directory=None, message=None, sql=False, head='head', splice=False,
             branch_label=None, version_path=None, rev_id=None):
    """Alias for 'revision --autogenerate'"""
    config = current_app.extensions['migrate'].migrate.get_config(
        directory, opts=['autogenerate'])
    if alembic_version >= (0, 7, 0):
        command.revision(config, message, autogenerate=True, sql=sql,
                         head=head, splice=splice, branch_label=branch_label,
                         version_path=version_path, rev_id=rev_id)
    else:
        command.revision(config, message, autogenerate=True, sql=sql)


def _edit(directory=None, revision='current'):
    """Edit current revision."""
    if alembic_version >= (0, 8, 0):
        config = current_app.extensions['migrate'].migrate.get_config(
            directory)
        command.edit(config, revision)
    else:
        raise RuntimeError('Alembic 0.8.0 or greater is required')


def _merge(directory=None, revisions='', message=None, branch_label=None,
           rev_id=None):
    """Merge two revisions together.  Creates a new migration file"""
    if alembic_version >= (0, 7, 0):
        config = current_app.extensions['migrate'].migrate.get_config(
            directory)
        command.merge(config, revisions, message=message,
                      branch_label=branch_label, rev_id=rev_id)
    else:
        raise RuntimeError('Alembic 0.7.0 or greater is required')


def _upgrade(directory=None, revision='head', sql=False, tag=None, x_arg=None):
    """Upgrade to a later version"""
    config = current_app.extensions['migrate'].migrate.get_config(directory,
                                                                  x_arg=x_arg)
    command.upgrade(config, revision, sql=sql, tag=tag)


def _downgrade(directory=None, revision='-1', sql=False, tag=None, x_arg=None):
    """Revert to a previous version"""
    config = current_app.extensions['migrate'].migrate.get_config(directory,
                                                                  x_arg=x_arg)
    if sql and revision == '-1':
        revision = 'head:-1'
    command.downgrade(config, revision, sql=sql, tag=tag)


def _show(directory=None, revision='head'):
    """Show the revision denoted by the given symbol."""
    if alembic_version >= (0, 7, 0):
        config = current_app.extensions['migrate'].migrate.get_config(
            directory)
        command.show(config, revision)
    else:
        raise RuntimeError('Alembic 0.7.0 or greater is required')


def _history(directory=None, rev_range=None, verbose=False):
    """List changeset scripts in chronological order."""
    config = current_app.extensions['migrate'].migrate.get_config(directory)
    if alembic_version >= (0, 7, 0):
        command.history(config, rev_range, verbose=verbose)
    else:
        command.history(config, rev_range)


def _heads(directory=None, verbose=False, resolve_dependencies=False):
    """Show current available heads in the script directory"""
    if alembic_version >= (0, 7, 0):
        config = current_app.extensions['migrate'].migrate.get_config(
            directory)
        command.heads(config, verbose=verbose,
                      resolve_dependencies=resolve_dependencies)
    else:
        raise RuntimeError('Alembic 0.7.0 or greater is required')


def _branches(directory=None, verbose=False):
    """Show current branch points"""
    config = current_app.extensions['migrate'].migrate.get_config(directory)
    if alembic_version >= (0, 7, 0):
        command.branches(config, verbose=verbose)
    else:
        command.branches(config)


def _current(directory=None, verbose=False, head_only=False):
    """Display the current revision for each database."""
    config = current_app.extensions['migrate'].migrate.get_config(directory)
    if alembic_version >= (0, 7, 0):
        command.current(config, verbose=verbose, head_only=head_only)
    else:
        command.current(config)


def _stamp(directory=None, revision='head', sql=False, tag=None):
    """'stamp' the revision table with the given revision; don't run any
    migrations"""
    config = current_app.extensions['migrate'].migrate.get_config(directory)
    command.stamp(config, revision, sql=sql, tag=tag)


@click.group()
def db():
    """Perform database migrations."""
    pass


@db.command()
@click.option('-d', '--directory', default=None,
              help=('migration script directory (default is "migrations")'))
@click.option('--multidb', is_flag=True,
              help=('Support multiple databases'))
def init(directory, multidb):
    """Creates a new migration repository."""
    _init(directory, multidb)


@db.command()
@click.option('-d', '--directory', default=None,
              help=('migration script directory (default is "migrations")'))
@click.option('-m', '--message', default=None, help='Revision message')
@click.option('--autogenerate', is_flag=True,
              help=('Populate revision script with andidate migration '
                    'operatons, based on comparison of database to model'))
@click.option('--sql', is_flag=True,
              help=('Don\'t emit SQL to database - dump to standard output '
                    'instead'))
@click.option('--head', default='head',
              help=('Specify head revision or <branchname>@head to base new '
                    'revision on'))
@click.option('--splice', is_flag=True,
              help=('Allow a non-head revision as the "head" to splice onto'))
@click.option('--branch-label', default=None,
              help=('Specify a branch label to apply to the new revision'))
@click.option('--version-path', default=None,
              help=('Specify specific path from config for version file'))
@click.option('--rev-id', default=None,
              help=('Specify a hardcoded revision id instead of generating '
                    'one'))
def revision(directory, message, autogenerate, sql, head, splice, branch_label,
             version_path, rev_id):
    """Create a new revision file."""
    _revision(directory, message, autogenerate, sql, head, splice,
              branch_label, version_path, rev_id)


@db.command()
@click.option('-d', '--directory', default=None,
              help=('migration script directory (default is "migrations")'))
@click.option('-m', '--message', default=None, help='Revision message')
@click.option('--sql', is_flag=True,
              help=('Don\'t emit SQL to database - dump to standard output '
                    'instead'))
@click.option('--head', default='head',
              help=('Specify head revision or <branchname>@head to base new '
                    'revision on'))
@click.option('--splice', is_flag=True,
              help=('Allow a non-head revision as the "head" to splice onto'))
@click.option('--branch-label', default=None,
              help=('Specify a branch label to apply to the new revision'))
@click.option('--version-path', default=None,
              help=('Specify specific path from config for version file'))
@click.option('--rev-id', default=None,
              help=('Specify a hardcoded revision id instead of generating '
                    'one'))
def migrate(directory, message, sql, head, splice, branch_label, version_path,
            rev_id):
    """Autogenerate a new revision file (Alias for 'revision --autogenerate')"""
    _migrate(directory, message, sql, head, splice, branch_label, version_path,
             rev_id)


@db.command()
@click.option('-d', '--directory', default=None,
              help=('migration script directory (default is "migrations")'))
@click.argument('revision', default='head')
def edit(directory, revision):
    """Edit a revision file"""
    _edit(directory, revision)


@db.command()
@click.option('-d', '--directory', default=None,
              help=('migration script directory (default is "migrations")'))
@click.option('-m', '--message', default=None, help='Merge revision message')
@click.option('--branch-label', default=None,
              help=('Specify a branch label to apply to the new revision'))
@click.option('--rev-id', default=None,
              help=('Specify a hardcoded revision id instead of generating '
                    'one'))
@click.argument('revisions', nargs=-1)
def merge(directory, message, branch_label, rev_id, revisions):
    """Merge two revisions together, creating a new revision file"""
    _merge(directory, revisions, message, branch_label, rev_id)


@db.command()
@click.option('-d', '--directory', default=None,
              help=('migration script directory (default is "migrations")'))
@click.option('--sql', is_flag=True,
              help=('Don\'t emit SQL to database - dump to standard output '
                    'instead'))
@click.option('--tag', default=None,
              help=('Arbitrary "tag" name - can be used by custom "env.py '
                    'scripts'))
@click.option('-x', '--x-arg', multiple=True,
              help='Additional arguments consumed by custom env.py scripts')
@click.argument('revision', default='head')
def upgrade(directory, sql, tag, x_arg, revision):
    """Upgrade to a later version"""
    _upgrade(directory, revision, sql, tag, x_arg)


@db.command()
@click.option('-d', '--directory', default=None,
              help=('migration script directory (default is "migrations")'))
@click.option('--sql', is_flag=True,
              help=('Don\'t emit SQL to database - dump to standard output '
                    'instead'))
@click.option('--tag', default=None,
              help=('Arbitrary "tag" name - can be used by custom "env.py '
                    'scripts'))
@click.option('-x', '--x-arg', multiple=True,
              help='Additional arguments consumed by custom env.py scripts')
@click.argument('revision', default='-1')
def downgrade(directory, sql, tag, x_arg, revision):
    """Revert to a previous version"""
    _downgrade(directory, revision, sql, tag, x_arg)


@db.command()
@click.option('-d', '--directory', default=None,
              help=('migration script directory (default is "migrations")'))
@click.argument('revision', default='head')
def show(directory, revision):
    """Show the revision denoted by the given symbol."""
    _show(directory, revision)


@db.command()
@click.option('-d', '--directory', default=None,
              help=('migration script directory (default is "migrations")'))
@click.option('-r', '--rev-range', default=None,
              help='Specify a revision range; format is [start]:[end]')
@click.option('-v', '--verbose', is_flag=True, help='Use more verbose output')
def history(directory, rev_range, verbose):
    """List changeset scripts in chronological order."""
    _history(directory, rev_range, verbose)


@db.command()
@click.option('-d', '--directory', default=None,
              help=('migration script directory (default is "migrations")'))
@click.option('-v', '--verbose', is_flag=True, help='Use more verbose output')
@click.option('--resolve-dependencies', is_flag=True,
              help='Treat dependency versions as down revisions')
def heads(directory, verbose, resolve_dependencies):
    """Show current available heads in the script directory"""
    _heads(directory, verbose, resolve_dependencies)


@db.command()
@click.option('-d', '--directory', default=None,
              help=('migration script directory (default is "migrations")'))
@click.option('-v', '--verbose', is_flag=True, help='Use more verbose output')
def branches(directory, verbose):
    """Show current branch points"""
    _branches(directory, verbose)


@db.command()
@click.option('-d', '--directory', default=None,
              help=('migration script directory (default is "migrations")'))
@click.option('-v', '--verbose', is_flag=True, help='Use more verbose output')
@click.option('--head-only', is_flag=True,
              help='Deprecated. Use --verbose for additional output')
def current(directory, verbose, head_only):
    """Display the current revision for each database."""
    _current(directory, verbose, head_only)


@db.command()
@click.option('-d', '--directory', default=None,
              help=('migration script directory (default is "migrations")'))
@click.option('--sql', is_flag=True,
              help=('Don\'t emit SQL to database - dump to standard output '
                    'instead'))
@click.option('--tag', default=None,
              help=('Arbitrary "tag" name - can be used by custom "env.py '
                    'scripts'))
@click.argument('revision', default='head')
def stamp(directory, sql, tag, revision):
    """'stamp' the revision table with the given revision; don't run any
    migrations"""
    _stamp(directory, revision, sql, tag)
