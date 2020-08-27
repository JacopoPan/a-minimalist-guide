#include <iostream>
#include "vehicles/multirotor/api/MultirotorRpcLibClient.hpp"

int main() {
    using namespace std;
    msr::airlib::MultirotorRpcLibClient client;

    cout << "Press Enter to enable API control" << endl; cin.get();
    client.enableApiControl(true);
    
    cout << "Press Enter to arm the drone" << endl; cin.get();
    client.armDisarm(true);

    cout << "Press Enter to takeoff" << endl; cin.get();
    client.takeoffAsync(5)->waitOnLastTask();

    cout << "Press Enter to move 5 meters in x direction with 1 m/s velocity" << endl; cin.get();  
    auto position = client.getMultirotorState().getPosition(); // from current location
    client.moveToPositionAsync(position.x() + 5, position.y(), position.z(), 1)->waitOnLastTask();

    cout << "Press Enter to land" << endl; cin.get();
    client.landAsync()->waitOnLastTask();
    return 0;
}