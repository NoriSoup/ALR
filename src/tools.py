import json
import math


def load_role_name():
    with open('json/role.json', 'r', encoding='utf-8') as fp:
        all_role_data = json.load(fp)
    return all_role_data.keys()


def load_role_data(role_name):
    with open('json/role.json', 'r', encoding='utf-8') as fp:
        all_role_data = json.load(fp)
    role_data = all_role_data[role_name]
    reload_data = role_data['reload']
    weapon_count = role_data['weapon_count']
    weapon_type = role_data['weapon_type']
    print(reload_data, weapon_count, weapon_type)
    return reload_data, weapon_count, weapon_type


def load_plane_name(weapon_type):
    with open('json/plane.json', 'r', encoding='utf-8') as fp:
        all_plane_data = json.load(fp)
    plane_name = all_plane_data[weapon_type]
    return plane_name


def load_plane_time(plane1, plane2, plane3):
    with open('json/plane.json', 'r', encoding='utf-8') as fp:
        all_plane_data = json.load(fp)
    all_plane_data = all_plane_data['7']
    plane_time = [all_plane_data[plane1], all_plane_data[plane2], all_plane_data[plane3]]
    print(plane_time)
    return plane_time


def compute_time(role_config, role_buff, is_world, neko_buff, neko_reload, tech_reload):
    print(role_config, role_buff, is_world, neko_buff, neko_reload, tech_reload)
    # 获取基础装填、武器数量
    role_data, weapon_count, weapon_type = load_role_data(role_config[0])

    # 获取舰载机冷却时间
    plane_time = load_plane_time(role_config[1], role_config[2], role_config[3])

    # 计算面板装填
    total_buff = 1.0
    if role_config[-1] == '100爱':
        panel_reload = role_data[0]
    elif role_config[-1] == '199婚':
        panel_reload = role_data[1]
    else:
        panel_reload = role_data[2]
    panel_reload = panel_reload + int(tech_reload)

    # 计算实际装填
    if role_buff:
        if is_world:
            total_buff = 1.04
        else:
            total_buff = 1.08
    if neko_buff:
        total_buff = total_buff + 0.01288
    actual_reload = panel_reload * total_buff + int(neko_reload)

    # 计算面板缩减
    panel_reduce = math.sqrt(200 / (panel_reload + 100))

    # 计算实际缩减
    actual_reduce = math.sqrt(200 / (actual_reload + 100))

    # 计算面板冷却
    panel_time = round((plane_time[0] * weapon_count[0] + plane_time[1] * weapon_count[1] + plane_time[2] *
                        weapon_count[2]) * panel_reduce / (weapon_count[0] + weapon_count[1] + weapon_count[2]) * 2.2,
                       2)

    actual_time = round((plane_time[0] * weapon_count[0] + plane_time[1] * weapon_count[1] + plane_time[2] *
                         weapon_count[2]) * actual_reduce / (weapon_count[0] + weapon_count[1] + weapon_count[2]) * 2.2,
                        2)

    print()
    print('panel_reduce is {}'.format(panel_reduce))

    print('{} : panel_time is {}s.'.format(role_config[0], panel_time))

    print('actual_reduce is {}'.format(actual_reduce))
    print('{} : actual_time is {}s.'.format(role_config[0], actual_time))

    return [role_config[0], panel_time, actual_time]


def judge_implacable(time_consume, is_world):
    if time_consume[0][0] == '怨仇':
        return '怨仇首飞，不利于调速。'
    if time_consume[2][0] == '怨仇':
        return '怨仇末飞，不利于调速。'

    if is_world:
        if (time_consume[1][2] - time_consume[0][2] >= 0.03) and (time_consume[2][2] - time_consume[1][2] >= 0.03):
            if time_consume[1][2] - time_consume[0][2] < 0.125:
                if time_consume[2][2] - time_consume[0][2] < 0.43:
                    return '该方案可行。'
                else:
                    return '首飞 与 怨仇 CD差小于 0.125s : 末飞 {} 与 首飞 {} CD差过大，建议保持在 0.43s 以内。'.format(time_consume[2][0],time_consume[0][0])
            elif 0.125 < time_consume[1][2] - time_consume[0][2] < 0.28:
                if time_consume[2][2] - time_consume[1][2] < 0.28:
                    return '该方案可行。'
                else:
                    return '首飞 与 怨仇 CD差小于 0.125s : 末飞 {} 与 首飞 {} CD差过大，建议保持在 0.43s 以内。'.format(time_consume[2][0],time_consume[0][0])
            else:
                return '怨仇 和 {} 的时间差过大了，建议保持在 0.28s 以内。'.format(time_consume[0][0])
        elif time_consume[1][2] - time_consume[0][2] < 0.03:
            return '首飞的 {} 与中飞的 {} 之间的空袭CD差小于0.03s，可能导致同帧错轴，建议调整。'.format(time_consume[0][0],
                                                                                                     time_consume[1][0])
        elif time_consume[2][2] - time_consume[1][2] < 0.03:
            return '末飞的 {} 与 {} 之间的空袭CD差小于0.03s，可能导致同帧错轴，建议调整。'.format(time_consume[2][0],
                                                                                               time_consume[1][0])
    else:
        if (time_consume[1][2] - time_consume[0][2] >= 0.03) and (time_consume[2][2] - time_consume[1][2] >= 0.03):
            if time_consume[1][2] - time_consume[0][2] < 0.166:
                if time_consume[2][2] - time_consume[0][2] < 0.5:
                    return '该方案可行。'
                else:
                    return '走方案一 : 末飞 {} 与 首飞 {} CD差过大，建议保持在 0.5s 以内。'.format(time_consume[2][0],time_consume[0][0])
            elif 0.166 < time_consume[1][2] - time_consume[0][2] < 0.37:
                if time_consume[2][2] - time_consume[1][2] < 0.34:
                    return '该方案可行。'
                else:
                    return '走方案二 : 末飞 {} 与 首飞 {} CD差过大，建议保持在 0.34s 以内。'.format(time_consume[2][0],time_consume[0][0])
            else:
                return '怨仇 和 {} 的时间差过大了，建议保持在 0.37s 以内。'.format(time_consume[0][0])
        elif time_consume[1][2] - time_consume[0][2] < 0.03:
            return '首飞的 {} 与中飞的 {} 之间的空袭CD差小于0.03s，可能导致同帧错轴，建议调整。'.format(time_consume[0][0],
                                                                                                     time_consume[1][0])
        elif time_consume[2][2] - time_consume[1][2] < 0.03:
            return '末飞的 {} 与 {} 之间的空袭CD差小于0.03s，可能导致同帧错轴，建议调整。'.format(time_consume[2][0],
                                                                                               time_consume[1][0])

    return '哒咩哟。'


def deal_compute(ships, role_buff, is_world, neko_buff, neko_reload, tech_reload):
    time_consume = []
    for ship in ships:
        time_consume.append(compute_time(ship, role_buff, is_world, neko_buff, neko_reload, tech_reload))
    time_consume = sorted(time_consume, key=lambda x: x[1])
    print(time_consume)
    return judge_implacable(time_consume, is_world)

