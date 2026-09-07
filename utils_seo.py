def tagClassCheck(tag):
  tag_classes = tag.get('class', [])
  return 'keywords' in tag_classes

def tagTypeCheck(tag):
  match tag[0].name:
    case 'meta':

      if tagClassCheck(tag[0]):
        content= [
          tag_item['content']
          for tag_item in tag
        ]

        return content
      else:
        content = tag[0]['content']

        return content

    case 'link':
      content = tag[0]['href']

      return content
    case _:
      content = tag[0].text.strip()

      return content

def check_valid(selector_list, html_soup):
  dict_tags = {}

  for css_path in selector_list:
    checking_tag = html_soup.select(css_path)
    quantity_tags = len(checking_tag)

    if quantity_tags > 0:
      content = tagTypeCheck(checking_tag)
    else:
      content = "n/a"

    dict_tags[css_path] = {     
      'content': content,
      'quantity': quantity_tags
    }
  return dict_tags