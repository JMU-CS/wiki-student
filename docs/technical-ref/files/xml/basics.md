# XML Basics

XML is a subset of the Standard Generalized Markup Language (SGML)
and, as such, is a meta-language that is used to create languages that
describe hierarchical data. XHTML (a variant of HTML) is one such
language that is used for mark-up papers/articles/books.

## Elements

XML has two different kind of elements, those that can contain component elements and those that can't. Both types can have attributes, which are name-value pairs.

XML elements that can't contain other elements have the following syntax (sometimes called the abbreviated syntax for empty elements):

`<tag [ attribute="value" ] ... />`

For example, the following might be such an element in a railroad
system:

``` xml
<Caboose id="857-931" type="limited" />
```

Elements that can contain other elements have the following syntax:

`<tag [ attribute="value" ] ... > [ component ... ] </tag>`

For example, the following might be such an element in a railroad system:

``` xml
  <Train id="321">
    <Caboose id="857-931" type="limited" />
  </Train>
```

Note that both tags and attribute names are case-sensitive. Note also that text strings can be components.

## Well-Formed XML Documents

An XML document is said to be well-formed if and only if:

- It only contain elements that have a start tag and a close tag or use the abbreviated syntax for empty elements;
- It has a single root element; and
- It has the XML declaration \<?xml version="1.0" ?\> as the first line.

The following is an example of a well-formed XML document in a railroad timetable system.

``` xml
<?xml version="1.0"?>
<timetable title="Boston...Providence...New London...New York"
     subtitle="Through services to Philadelphia...Washington...Newport News">
  <train number="95" normaldays="Mo-Fr" reservations="YES" businessclass="YES">
    <stop>
      <station>Boston, MA-South Station</station>
      <time>6:20AM</time>
    </stop>

    <stop>
      <station>Newport News, VA</station>
      <time status="Ar">7:07PM</time>
    </stop>
  </train>

  <train number="191" normaldays="Sa"  reservations="YES" businessclass="YES">
    <stop>
      <station>Boston, MA-South Station</station>
      <time>6:20AM</time>
    </stop>

    <stop>
      <station>Newport News, VA</station>
      <time></time>
    </stop>
  </train>
</timetable>
```

## Imposing Structure

To be well-formed an XML document must satisfy a few simple requirements. However, these requirements say nothing about the structure of the document (e.g., the attributes for each element, the hierarchical structure of the elements).

There are two different ways to impose structure. One is to use a Document Type Definition (DTD) and the other is to use a Schema. Thought they have very different syntaxes, they are conceptually very similar.

For example, the following DTD:

``` dtd
<!ELEMENT timetable (train*) >
  <!ATTLIST timetable subtitle CDATA #IMPLIED>
  <!ATTLIST timetable title CDATA #IMPLIED>



<!ELEMENT station (#PCDATA) >

<!ELEMENT stop (station, time*) >



<!ELEMENT time (#PCDATA) >
  <!ATTLIST time status (Ar | Dp) #IMPLIED>


<!ELEMENT train (stop+) >
  <!ATTLIST train businessclass (YES | NO) "NO" >
  <!ATTLIST train normaldays (Daily | Mo-Fr | Sa | Su) #REQUIRED >
  <!ATTLIST train number CDATA #REQUIRED >
  <!ATTLIST train reservations (YES | NO) "NO" >
```

and the following Schema:

``` xml
<?xml version="1.0" ?>
<Schema name="timetable_schema"
        xmlns="urn:schemas-microsoft-com:xml-data"
        xmlns:dt="urn:schemas-microsoft-com:datatypes">

  <ElementType name="timetable" content="eltOnly" model="closed">
    <description>The root element</description>
    <element type="train" minOccurs="1" maxOccurs="*" />
    <AttributeType name="subtitle" dt:type="string" required="no" />
    <AttributeType name="title" dt:type="string" required="no" />
    <attribute type="title" />
    <attribute type="subtitle" />
  </ElementType>

  <ElementType name="station" content="textOnly" 
               dt:type="string" model="closed" />

  <ElementType name="stop" content="eltOnly" model="closed">
    <element type="station" minOccurs="1" maxOccurs="1" />
    <element type="time"    minOccurs="0" maxOccurs="*" />
  </ElementType>


  <ElementType name="time" content="textOnly"
               dt:type="string" model="closed" >
    <AttributeType name="status" required="no" 
                   dt:type="enumeration" dt:values="Ar Dp"/>
    <attribute type="status" />
  </ElementType>


  <ElementType name="train" content="eltOnly" model="closed">
    <element type="stop" minOccurs="1" maxOccurs="*" />
    <AttributeType name="businessclass" required="no" default="NO"
                   dt:type="enumeration" dt:values="YES NO"/>
    <AttributeType name="normaldays" required="yes"
                   dt:type="enumeration" dt:values="Daily Mo-Fr Sa Su"/>
    <AttributeType name="number" dt:type="string" required="yes" />
    <AttributeType name="reservations" required="no" default="NO"
                   dt:type="enumeration" dt:values="YES NO"/>
    <attribute type="businessclass" />
    <attribute type="normaldays" />
    <attribute type="number" />
    <attribute type="reservations" />
  </ElementType>

</Schema>
```

can both be used to impose structure on a railroad timetable document.

The primary advantage of Schemas is that they are also written in XML, which means that the same parser can be used for the data document and the document that describes its structure.
