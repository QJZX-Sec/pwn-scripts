from urllib import request
from json import dumps as jsonMarshal, load as jsonUnMarshal
from argparse import ArgumentParser


class Request_Info_Failed(Exception):
  pass


class Get_Info_Failed(Exception):
  pass


def get_app_info(app_id: int) -> tuple[str, str, str]:
  '''
  give the `app_id` to get the `app_name`, `apk_url` and `res_url`,
  the `.rpk` file from `res_url` is for the path `/storage/0/Android/obb`
  '''
  resp = request.urlopen(request.Request(
      "http://tools.huluxia.com/game/detail/ANDROID/4.1.5?app_id={}".format(app_id), method="GET"))
  if resp.code != 200:
    raise Request_Info_Failed(
        "request is not successful,", resp.code, resp.reason)
  resp_json = jsonUnMarshal(resp)
  resp.close()
  if resp_json["status"] != 1:
    raise Get_Info_Failed("app_id is not accessible",
                          jsonMarshal(resp_json, ensure_ascii=False))
  app_name: str = resp_json["gameinfo"]["apptitle"]
  apk_url: str = resp_json["gameinfo"]["localurl"]["url"]
  res_url: str = resp_json["gameinfo"]["dataDownUrl"]
  return app_name, apk_url, res_url if res_url else ""


if __name__ == "__main__":
  arg_parser = ArgumentParser("get_real_download_link_from_huluxia.py",
                              usage="give the app_id from the shared link and you can get the real download link of the resource from HuLuXia")
  arg_parser.add_argument("-id", "--app_id", required=True,
                          type=int, help="the `app_id` you got from shared link")
  args = arg_parser.parse_args()
  app_name, apk_url, res_url = get_app_info(args.app_id)
  print("app_name: {}".format(app_name))
  print("apk_url: {}".format(apk_url))
  print("res_url: {}".format(res_url))
