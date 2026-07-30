project = 'Eset Home Secuirty'
copyright = '2026'
author = 'Admin'

extensions = [ 'sphinx.ext.autodoc',
               'sphinx.ext.napoleon',
               'sphinx_sitemap',
              ]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'alabaster' # Screenshot wala classic white theme

html_baseurl = 'https://communities-anytime-esethome.readthedocs-hosted.com/en/latest/'
sitemap_url_scheme = "{link}"

# conf.py

html_title = "[KB3419] Download ESET Internet Security"
html_short_title = "ESET Internet Security free trial"
html_static_path = ['_static']
html_extra_path = ['_static/google5ffeff63dcb91d99.html'] 


# Meta Tags Configuration
html_context = {
    'metatags': '''
        <meta name="description" content="Download Your ESET Internet Security free trial today. Full setup guide covers install, activation, and fixes for common errors on Windows 10/11.">
        <meta name="[KB3419] Download ESET Internet Security free trial" content="docs, guide, setup, tutorial">
     
    '''
}
