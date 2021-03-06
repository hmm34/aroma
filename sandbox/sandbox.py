from lxml import etree
'''
ns = {'src': 'http://www.sdml.info/srcML/src',
                  'cpp': 'http://www.sdml.info/srcML/cpp'}
'''

inputXML = etree.parse('../test/pull_up_function/pull_up.xml')

'''
result = inputXML.xpath("//src:private/src:aroma[@refactor='pull_up' and @role='source']/src:decl_stmt",
              namespaces=ns)

print len(result)

fields = []

for res in result:
  print res.tag
  field = etree.tostring(res).replace(' xmlns="http://www.sdml.info/srcML/src" xmlns:cpp="http://www.sdml.info/srcML/cpp"', '')
  if field not in fields:
    fields.append(field)

result2 = inputXML.xpath("//src:aroma[@refactor='pull_up' and @role='destination']/src:class/src:block/src:protected",
                     namespaces=ns)

print len(result2)
'''

xsltcode = '''<xsl:stylesheet
   xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
   xmlns:src="http://www.sdml.info/srcML/src"
   xmlns="http://www.sdml.info/srcML/src"
   xmlns:cpp="http://www.sdml.info/srcML/cpp"
   xmlns:str="http://exslt.org/strings"
   xmlns:func="http://exslt.org/functions"
   xmlns:exsl="http://exslt.org/common"
   extension-element-prefixes="str exsl func"
   exclude-result-prefixes="src"
   version="1.0">

   <xsl:output method="xml" omit-xml-declaration="no" version="1.0" encoding="UTF-8"/>

   <xsl:template match="@* | node()" name="identity">
      <xsl:copy>
         <xsl:apply-templates select="@* | node()"/>
      </xsl:copy>
   </xsl:template>
'''


xsltcode += '''<xsl:template match="//src:aroma[@refactor='remove']" xml:space="preserve"/>'''

#for field in fields:
#  xsltcode += field.replace(' ', '<xsl:text>&#032;</xsl:text>')
#  xsltcode += '''<xsl:text>&#xa;</xsl:text>'''

#xsltcode += '''</xsl:template>'''

#xsltcode += '''<xsl:template match="//src:aroma[@refactor='pull_up' and @role='source']"/>'''

xsltcode += '</xsl:stylesheet>'

xslt_root = etree.XML(xsltcode)
transform = etree.XSLT(xslt_root)
outputXML = transform(inputXML)

print(etree.tostring(outputXML))
