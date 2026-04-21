import abc

class Creator(abc.ABC):
    def __init__(self, name, platform, **kwargs):
        self.name = name
        self.platform = platform
        super().__init__(**kwargs)

    abc.abstractmethod
    def create_content(self):
        print("This shit will work")


class PodcastHost(Creator):
    def __init__(self , topic, **kwargs):
        super().__init__(**kwargs)
        self.topic = topic
    def record_episode(self):
        return f"{self.name} records a podcast episode about {self.topic}."
    def create_content(self):
        return "This podcast is still in progress."

class TravelWriter(Creator):
    def __init__(self,  region, **kwargs):
        super().__init__( **kwargs)
        self.region = region
    def write_article(self):
        return f"{self.name} writes travel article about  {self.region}."
    def create_content(self):
       return  "Travel article in progress."



class FieldReporter(PodcastHost, TravelWriter):
    def __init__(self, name, platform, topic, region):
        super().__init__(
            name = name,
            platform=platform,
            topic = topic,
            region= region
        )

    def create_content(self):
        return "Mixed content for now"


    
travel = FieldReporter("Timo", "yt", "Tanks", "Spain")

#print("writing article ", travel.write_article())
#print("Recording ep: ", travel.record_episode())
#print("CONTENT ", travel.create_content())
#print(FieldReporter.mro())
#print(travel)





class CameraCreator(Creator):
    def __init__(self, camera, **kwargs):
        super().__init__(**kwargs)
        self.camera = camera
    def publish(self):
        print("Photo story published")
    def create_content(self):
        print(f"He creates content with {self.camera}")

class AudioCreator(Creator):
    def __init__(self,audio, **kwargs):
        super().__init__(**kwargs)
        self.audio = audio
    
    def publish(self):
        print("Audio story published")
    
    def create_content(self):
        print(f"He creates content with {self.audio}")

class HybridCreator( CameraCreator, AudioCreator):
    def __init__(self, name, platform, camera, audio):
        super().__init__(name = name, platform = platform, camera = camera, audio= audio)

    def create_content(self):
        return super().create_content()
    


h = HybridCreator("Timo", "YT", "Cannon", "MX5")
h.publish()

h.create_content()

print(HybridCreator.mro())