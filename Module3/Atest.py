from abc import ABC, abstractmethod

class IOpperator(ABC):
    def __init__(self, name, platform, **kwargs):
        self.name = name
        self.platform = platform
        super().__init__(**kwargs)

    @abstractmethod
    def type_of_platform(self):
        pass


class Newspaper(IOpperator):
    def __init__(self, date, **kwargs):
        self.date = date

        super().__init__(**kwargs)
    
    def type_of_platform(self):
        return f"The {self.platform} will air now"
    
    def release_date_of_newspaper(self):
        return f"News will release on {self.date}"
    
class YTNews(IOpperator):
    def __init__(self, channel, **kwargs):
        self.channel = channel
        super().__init__(**kwargs)
    def type_of_platform(self):
        return f"The {self.platform} will air now"
    def release_time_of_yt_video(self):
        return f"The youtube video will release on the {self.channel} channel"
    
class Opperation_Manager(YTNews, Newspaper):
    def __init__(self, name, platform, channel, date):
        super().__init__(name = name, platform= platform, channel = channel, date = date)
    def type_of_platform(self):
        return "Opperation manager platform"


name = "News.0"
platform = "Youtube"
channel = "News.0"
date = "22.04.2026"
class_call = Opperation_Manager(name,platform, channel, date)
print(class_call.release_time_of_yt_video())
print(class_call.release_date_of_newspaper())
print(Opperation_Manager.mro())