import request from '@/utils/request'

export function fetchRobotList() {
  return request({
    url: '/robots/discovery',
    method: 'get'
  })
}

export function set_config_diff(data) {
  return request({
    url: '/robots/set_diff_config_by_id',
    method: 'put',
    data
  })
}

export function set_config_same(data) {
  return request({
    url: '/robots/set_same_config_by_id',
    method: 'put',
    data
  })
}

export function get_config_all(data) {
  return request({
    url: '/robots/get_config_for_all',
    method: 'post',
    data
  })
}

export function updateWifi(data) {
  return request({
    url: '/robots/set_wifi_hotspot',
    method: 'post',
    data
  })
}

export function fetchWifi() {
  return request({
    url: '/robots/get_wifi_hotspot',
    method: 'get'
  })
}
