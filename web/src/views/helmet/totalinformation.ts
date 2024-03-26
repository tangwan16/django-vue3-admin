import { request } from '/@/utils/service';

export function getTotalInfo () {
    return request({
      url:'http://localhost:9091/totalinformation/all',
    })
  };
  
  
  export function updateTotalInfo(){
    return request({
      url:'http://localhost:9091/totalinformation/update',
    })

  };