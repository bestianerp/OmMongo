import sys, os

sys.path.insert(0, os.path.abspath('..'))

html_theme = 'flask'

# -- General configuration -----------------------------------------------------

locale_dirs             = ['locale/']
gettext_compact         = False
extensions              = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.coverage', 'sphinx.ext.viewcode']
templates_path          = ['_templates']
source_suffix           = '.txt'
master_doc              = 'index'
project                 = u'OmMongo'
copyright               = u'2017, Bapakode Open Source'
version                 = '0.1'
release                 = '0.1'
exclude_patterns        = ['build', '_static', '_templates']
pygments_style          = 'sphinx'
autoclass_content       = 'both'
autodoc_member_order    = 'bysource'
autodoc_default_flags   = ['members', 'inherited-members', 'undoc-members']

# -- Options for HTML output ---------------------------------------------------

html_static_path    = ['static']
htmlhelp_basename   = 'OmMongo'

#html_theme          = "sphinx_rtd_theme"
#html_theme_path     = [sphinx_rtd_theme.get_html_theme_path()]

# -- Options for LaTeX output --------------------------------------------------

latex_documents = [('index', 'OmMongo.tex', u'OmMongo Documentation',u'Bapakode Open Source', 'manual')]

# -- Options for manual page output --------------------------------------------

man_pages   = [('index', 'OmMongo', u'OmMongo Documentation',[u'OmMongo Open Source'], 1)]

bad_names   = ['schema_json', 'has_autoload', 'set_parent_on_subtypes', 
                'subfields', 'has_subfields', 'valid_modifiers',
                'set_value', 'update_ops', 'db_field', 'no_real_attributes',
                'default', 'localize', 'auto', 'dirty_ops', 'validate_wrap',
                'is_valid_unwrap', 'is_valid_wrap', 'unwrap', 
                'validate_unwrap', 'wrap', 'wrap_value', 'PrimitiveField',
                'NumberField', 'SequenceField', 'child_type',
                'type', 'sub_type', 'compute_value', 'in_transaction',
                'autoflush', 'cache_write', 'cache_read', 'transaction_id',
                'execute_update', 'execute_remove', 'execute_find_and_modify']

bad_exc     = ['message', 'args']

def skip_common(app, what, name, obj, skip, options):
    print what, name, obj
    if what == 'exception' and name in bad_exc:
        return True
    if name in bad_names:
        return True
    return skip

def setup(app):
    app.connect('autodoc-skip-member', skip_common)


