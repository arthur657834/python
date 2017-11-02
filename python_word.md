安装win32

```python
#coding:utf-8
import win32com
from win32com.client import Dispatch, constants
wordApp = win32com.client.Dispatch('Word.Application')


wordApp.Visible = True
wordApp.DisplayAlerts = 0

doc = wordApp.Documents.Add() 
# doc = wordApp.Documents.Open(filename) 
doc.Paragraphs.Last.Range.Text = 'hello ljtest!'

myRange = doc.Range(1, 1)
myRange.InsertBefore('1')

myRange2 = doc.Range(doc.Content.Start, doc.Content.end)
myRange2.InsertBefore('2')

range = doc.Range()
range.InsertBefore('king')
range.InsertAfter(doc.Content)

wordApp.Selection.Find.ClearFormatting()  
wordApp.Selection.Find.Replacement.ClearFormatting() 
# replace
# wordApp.Selection.Find.Execute('king', False, False, False, False, False, True, 1, True, 'arthur', 2) 
print  wordApp.Selection.Find.Execute('king') 
print  wordApp.Selection.Find.Execute('arthur') 
doc.SaveAs('d://say_hello.docx')
# doc.Save()


doc.Close()
wordApp.Quit()
```
