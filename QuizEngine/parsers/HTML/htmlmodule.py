def htmlmodule(website, file_name):
    module = import_by_string("QuizEngine.parsers.HTML.websites."+website+"."+website)

    htmlparser = module()
    with open(file_name, 'r') as fp:
        big_json = htmlparser.feed(fp.readlines())
        return big_json

def import_by_string(full_name):
    module_name, unit_name = full_name.rsplit('.', 1)
    return getattr(__import__(module_name, fromlist=['']), unit_name)