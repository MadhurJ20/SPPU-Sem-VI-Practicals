<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <head>
                <style>
                    table {
                    width: 100%;
                    border-collapse: collapse;
                    }
                    th, td {
                    border: 1px solid #ddd;
                    padding: 8px;
                    }
                    tr:nth-child(even) {
                    background-color: #f2f2f2;
                    }
                    th {
                    padding-top: 12px;
                    padding-bottom: 12px;
                    text-align: left;
                    background-color: #4CAF50;
                    color: white;
                    }
                </style>
            </head>
            <body>
                <table>
                    <tr>
                        <th>Name</th>
                        <th>Position</th>
                        <th>Department</th>
                    </tr>
                    <xsl:for-each select="employees/employee">
                        <tr>
                            <td><xsl:value-of select="name"/></td>
                            <td><xsl:value-of select="position"/></td>
                            <td><xsl:value-of select="department"/></td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>