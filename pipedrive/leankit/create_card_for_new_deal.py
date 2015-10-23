
# Create new leankit card for Pipedrive deal.
{
    "connector_in":"Pipedrive, v1.0",
    "new_mapper":"
        # function convert date input format to date output format.
        def get_date_in_out_format(input_date):
            date_result = ''
            if input_date:
                input_date = input_date.split('-')
            date_result = '/'.join([
                input_date[1], input_date[2], input_date[0]])
        return date_result
        in_data = in_dict.get('data')
        finish_date = in_data.get('expected_close_date')
        start_date = in_data.get('next_activity_date')
        # dct_types_card contains custom types of pipedrive activities  
        # and numbers of types of leankit cards.
        dct_types_card = {'new_feature': Insert_leankt_type_card_here, 'risk__issue': Insert_leankt_type_card_here}
        type_card = in_data.get('next_activity_type')
        out_dict = {
            'Title': in_data.get('title'),
            'Description': in_data.get('next_activity_note'),
            'Size': in_data.get('value'),
            'Tags': in_data.get('next_activity_subject'),
            'DueDate': get_date_in_out_format(finish_date),
            'StartDate': get_date_in_out_format(start_date),
            'ExternalCardID': str(in_data.get('id')),
            'ExternalSystemName': in_data.get('org_name'),
            'TypeId': dct_types_card.get(type_card),
        }",
    "name":"github_1",
    "parameters_out":{
        "url":"Insert_your_hostname_here",
        "user":{
            "password":"Insert_your_account_password_here",
            "login":"Insert_your_email_address_here"
        },
        "optional":{
            "board_id":"Insert_board_id_here",
            "lane_id":"Insert_lane_id_here",
            "position":"Insert_position_card_in_board_here"
        },
        "command":"AddCard"
    },
    "connector_out":"Leankit Kanban, v1.0",
    "parameters_in":{
        "error_codes":[
            501,
            401
        ],
        "http_method":"GET",
        "rest_data":{},
        "api_method":"/deals/insert_your_id_deal_here",
        "api_url":"https://api.pipedrive.com/v1",
        "api_token":"Insert_your_api_token_here"
    }
}
