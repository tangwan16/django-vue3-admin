import { request } from '/@/utils/service';


export function updateUWB () {
  return request({
    url:'http://localhost:9091/uwb/update',
    method:'POST'
  })
};







