import time


class Vehicle:
    def _init_(self, name, position, speed):
        self.name = name
        self.position = position
        self.speed = speed

    def update_position(self, time_interval):
        self.position += self.speed * time_interval

    def _str_(self):
        return f"{self.name} - Position: {self.position}, Speed: {self.speed}"


class Platoon:
    def _init_(self, leader, followers):
        self.leader = leader
        self.followers = followers

    def update_positions(self, time_interval):
        self.leader.update_position(time_interval)

        for follower in self.followers:
            follower.position = self.leader.position

    def add_follower(self, follower):
        self.followers.append(follower)

    def remove_follower(self, follower):
        self.followers.remove(follower)

    def _str_(self):
        leader_info = f"Leader: {str(self.leader)}"
        followers_info = [str(follower) for follower in self.followers]
        followers_info = "\n".join(followers_info)

        return f"{leader_info}\nFollowers:\n{followers_info}"


def simulate_platooning(platoon, duration, time_interval):
    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        platoon.update_positions(time_interval)
        print(platoon)
        time.sleep(time_interval)


# Create vehicles
leader: Vehicle = Vehicle("Leader", 0, 60)
follower1 = Vehicle("Follower 1", 0, 0)
follower2 = Vehicle("Follower 2", 0, 0)
joiner = Vehicle("Joiner", 0, 40)

# Create platoon with leader and followers
platoon = Platoon(leader, [follower1, follower2])

# Add joiner vehicle to the platoon
platoon.add_follower(joiner)

# Simulate platooning for 10 seconds with 1-second time interval
simulate_platooning(platoon, 10, 1)