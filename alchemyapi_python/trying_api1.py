

from __future__ import print_function
from alchemyapi import AlchemyAPI
import json


demo_text = ''
demo_url='https://en.wikipedia.org/wiki/Amgen'

# Create the AlchemyAPI Object
alchemyapi = AlchemyAPI()

print('#   Entity Extraction Example              #')


response = alchemyapi.text('url', demo_url)
demo_text = response['text'].encode('utf-8')
print('')

response = alchemyapi.entities('text', demo_text, {'sentiment': 1})

if response['status'] == 'OK':
    print('## Response Object ##')
    with open('entities.js', 'w') as outfile:
        json.dump(response,outfile, indent=4)

    print('## Entities ##')
    for entity in response['entities']:
        print('text: ', entity['text'].encode('utf-8'))
        print('type: ', entity['type'])
        print('relevance: ', entity['relevance'])
        print('sentiment: ', entity['sentiment']['type'])
        if 'score' in entity['sentiment']:
            print('sentiment score: ' + entity['sentiment']['score'])
        print('')
else:
    print('Error in entity extraction call: ', response['statusInfo'])



print('')
print('')
print('#   Keyword Extraction Example             #')
print('')

response = alchemyapi.keywords('text', demo_text, {'sentiment': 1})

if response['status'] == 'OK':
    print('## Response Object ##')
    with open('keyword.js', 'w') as outfile:
        json.dump(response,outfile, indent = 4)
    print('')
    print('## Keywords ##')
    for keyword in response['keywords']:
        print('text: ', keyword['text'].encode('utf-8'))
        print('relevance: ', keyword['relevance'])
        print('sentiment: ', keyword['sentiment']['type'])
        if 'score' in keyword['sentiment']:
            print('sentiment score: ' + keyword['sentiment']['score'])
        print('')
else:
    print('Error in keyword extaction call: ', response['statusInfo'])





print('')
print('')
print('#   Concept Tagging Example                #')


response = alchemyapi.concepts('text', demo_text)

if response['status'] == 'OK':
    print('## Object ##')
    with open('Concept.js', 'w') as outfile:
        json.dump(response,outfile, indent =4 )

    print('')
    print('## Concepts ##')
    for concept in response['concepts']:
        print('text: ', concept['text'])
        print('relevance: ', concept['relevance'])
        print('')
else:
    print('Error in concept tagging call: ', response['statusInfo'])



print('')
print('')

print('#   Sentiment Analysis Example             #')

print('')

response = alchemyapi.sentiment('text', demo_text)

if response['status'] == 'OK':
    print('## Response Object ##')
    with open('sentiment.js', 'w') as outfile:
        json.dump(response,outfile)

    print('')
    print('## Document Sentiment ##')
    print('type: ', response['docSentiment']['type'])

    if 'score' in response['docSentiment']:
        print('score: ', response['docSentiment']['score'])
else:
    print('Error in sentiment analysis call: ', response['statusInfo'])


print('')
print('')

print('#   Title Extraction Example               #')

print('Processing url: ', demo_url)
print('')

response = alchemyapi.title('url', demo_url)

if response['status'] == 'OK':
    print('## Response Object ##')
    with open('title.js', 'w') as outfile:
        json.dump(response,outfile)

    print('')
    print('## Title ##')
    print('title: ', response['title'].encode('utf-8'))
    print('')
else:
    print('Error in title extraction call: ', response['statusInfo'])



print('')
print('')

print('#   Relation Extraction Example            #')

#print('Processing text: ', demo_text)
print('')

response = alchemyapi.relations('text', demo_text)

if response['status'] == 'OK':
    print('## Object ##')
    with open('relation-extract.js', 'w') as outfile:
        json.dump(response,outfile, indent =4 )

    print('')
    print('## Relations ##')
    for relation in response['relations']:
        if 'subject' in relation:
            print('Subject: ', relation['subject']['text'].encode('utf-8'))

        if 'action' in relation:
            print('Action: ', relation['action']['text'].encode('utf-8'))

        if 'object' in relation:
            print('Object: ', relation['object']['text'].encode('utf-8'))

        print('')
else:
    print('Error in relation extaction call: ', response['statusInfo'])


print('')
print('')
print('')
   
print('#   Text Categorization Example            #')

#print('Processing text: ', demo_text)
print('')

response = alchemyapi.category('text', demo_text)

if response['status'] == 'OK':
    print('## Response Object ##')
    with open('text_cat.js', 'w') as outfile:
        json.dump(response,outfile)

    print('')
    print('## Category ##')
    print('text: ', response['category'])
    print('score: ', response['score'])
    print('')
else:
    print('Error in text categorization call: ', response['statusInfo'])



##
##print('#   Feed Detection Example                 #')
##
##
##print('Processing url: ', demo_url)
##print('')
##
##response = alchemyapi.feeds('url', demo_url)
##
##if response['status'] == 'OK':
##    print('## Response Object ##')
##    with open('feed detection.js', 'w') as outfile:
##        json.dump(response,outfile, indent =4)
##
##    print('')
##    print('## Feeds ##')
##    for feed in response['feeds']:
##        print('feed: ', feed['feed'])
##else:
##    print('Error in feed detection call: ', response['statusInfo'])
##
##
##


print('')
print('')
print('#   Microformats Parsing Example           #')


#print('Processing url: ', demo_url)
print('')

response = alchemyapi.microformats('url', demo_url)

if response['status'] == 'OK':
    print('## Response Object ##')
    with open('microformats.txt', 'w') as outfile:
        json.dump(response,outfile, indent =4)

    print('')
    print('## Microformats ##')
    for microformat in response['microformats']:
        print('Field: ', microformat['field'].encode('utf-8'))
        print('Data: ', microformat['data'])
        print('')

else:
    print('Error in microformats parsing call: ', response['statusInfo'])


print('')
print('')


print('#   Taxonomy  Example                      #')

response = alchemyapi.taxonomy('text', demo_text)

if response['status'] == 'OK':
    print('## Response Object ##')
    with open('taxonomy.js', 'w') as outfile:
        json.dump(response,outfile, indent =4)

    print('')
    print('## Categories ##')
    for category in response['taxonomy']:
        print(category['label'], ' : ', category['score'])
    print('')

else:
    print('Error in taxonomy call: ', response['statusInfo'])




print('')
print('')


print('#   Combined  Example                      #')

response = alchemyapi.combined('text', demo_text)

if response['status'] == 'OK':
    print('## Response Object ##')
    with open('combied.js', 'w') as outfile:
        json.dump(response,outfile, indent =4)

    print('')

    print('## Keywords ##')
    for keyword in response['keywords']:
        print(keyword['text'], ' : ', keyword['relevance'])
    print('')

    print('## Concepts ##')
    for concept in response['concepts']:
        print(concept['text'], ' : ', concept['relevance'])
    print('')

    print('## Entities ##')
    for entity in response['entities']:
        print(entity['type'], ' : ', entity['text'], ', ', entity['relevance'])
    

else:
    print('Error in combined call: ', response['statusInfo'])

print('')
print('')
