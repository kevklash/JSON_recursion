from data import data

def _recursive_aggregation(input_data: dict, params: list, param_index: int, return_dict: dict):
  output_data = return_dict

  if param_index == 0:
    # create first level
    for index, element in enumerate(input_data, start=1):
        output_data.update({element[params[0]]: {}})
        amount: int = 0
        if param_index == len(params) - 1:
            output_data[element[params[param_index]]].update(
                {'amount': amount + element['amount']})
    if param_index == len(params) - 1:
      return output_data
    else:
        return _recursive_aggregation(input_data, params, param_index + 1,
                               output_data)

  if param_index == 1:
    # build second level
    for k, v in output_data.items():
        for index, element in enumerate(input_data, start=1):
            if element[params[param_index - 1]] == k:
                output_data[k].update({element[params[param_index]]: {}})
                amount: int = 0
                if param_index == len(params) - 1:
                    output_data[k][element[params[param_index]]].update(
                        {'amount': amount + element['amount']})
    if param_index == len(params) - 1:
        return output_data
    else:
        return _recursive_aggregation(input_data, params, param_index + 1,
                               output_data)

  if param_index == 2:
    # build third level
    for k, v in output_data.items():  # first level
        for element in output_data[k].items():  # scnd level
            for index_, value_ in enumerate(input_data, start=1):
                # print(value_, 'value') # prints the row from raw data
                # print(element[0]) # prints the key name, since it is a tupple
                # print(value_[params[2]]) # prints the value for the third param from raw data
                if value_[params[1]] == element[
                        0]:  # second level key(second param) == key name in second level of output
                    output_data[k][element[0]].update(
                        {value_[params[2]]: {}})
                    # amount
                    amount: int = 0
                    # sumar
                    output_data[k][element[0]][value_[params[2]]].update(
                        {'amount': amount + value_['amount']})
    return output_data


def aggregate(input_data: dict, params: list):
  return _recursive_aggregation(input_data, params, 0, {})


if __name__ == '__main__':
  print('-----------------------')
  # print(_recursive_aggregation(data, ['country', 'city'], 0, {}))
  print(aggregate(data, ['country', 'city']))
