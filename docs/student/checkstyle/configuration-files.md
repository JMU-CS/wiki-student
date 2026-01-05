

===== Checkstyle Configuration Files =====


A Checkstyle configuration file is a description of how a Java source
file should be analyzed. They are written
in XML and consist of principally of
''%%module%%'' elements.


The root element of every configuration is a ''%%module%%'' with 
a name of ''%%"Checker"%%''.


==== Adding Checks ====


The most important element inside of the root element is a module with a name   of ''%%"TreeWalker"%%'' which, itself, contains the actual checks.   It's name indicates that the checks it contains involve traversing the parse   tree of the Java source file.


So, for example, a typical configuration file would be something like the
following:

<code xml>
<module name="Checker">
  <module name="TreeWalker">

  <!-- Check Elements -->

  </module>
</module>
</code>

The ''%%"TreeWalker"%%'' element contains ''%%module%%''   elements that define the checks to perform. (It can also contain   ''%%property%%'' elements that dictate things like the file type   to use to identify Java source files.)

For example, the following configuration file instructs Checkstyle to   check if source files inappropriately use the ''%%*%%''   wildcard in imports.

<code xml>
<module name="Checker">
  <module name="TreeWalker">
    <module name="AvoidStarImport"/>
  </module>
</module>
</code>

Many checks have ''%%property%%'' elements that control how they behave.   For example, the following check restricts the number of logical operators   that can be included in a Boolean expression to seven.

<code xml>
    <module name="BooleanExpressionComplexity">
      <property name="max" value="7"/>
    </module>
</code>

For more information about the kinds of checks that can be performed,   see the [[ http://checkstyle.sourceforge.net/checks.html |    on-line documentation ]].


==== Filtering Files ====


Style guidelines don't always apply to all files. For example, many   organizations do not require that style guideline be followed for   JUnit tests. In such cases, one can include a   ''%%"BeforeExecutionFileFilter"%%'' element inside of   the ''%%"Checker"%%'' element.


For more information see the
[[ http://checkstyle.sourceforge.net/config_filefilters.html | 
on-line documentation. ]]