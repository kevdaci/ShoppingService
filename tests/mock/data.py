request_data = {
    "items": [
        {
            "name": "orange",
            "quantity": 3
        },
        {
            "name": "apple",
            "quantity": 4
        }
    ]
}

mock_orders = { 
	"orders": [
		{
            "order_id": "ed854482-89a1-4423-aff6-91991a389e46",
            "summary": [
                {
                    "cost": 0.5,
                    "name": "orange",
                    "quantity": 2
                },
                {
                    "cost": 1.2,
                    "name": "apple",
                    "quantity": 4
                }
            ],
            "total": 1.7
        },
        {
            "order_id": "a70b5329-0cb9-42b7-bfd3-1c4392bf60cc",
            "summary": [
                {
                    "cost": 0.5,
                    "name": "orange",
                    "quantity": 3
                },
                {
                    "cost": 1.2,
                    "name": "apple",
                    "quantity": 4
                }
            ],
            "total": 1.7
        },
        {
            "order_id": "6b0d5ff2-d64d-4e57-9ed5-14a790527aff",
            "summary": [
                {
                    "cost": 0.5,
                    "name": "orange",
                    "quantity": 3
                },
                {
                    "cost": 0.6,
                    "name": "apple",
                    "quantity": 1
                }
            ],
            "total": 1.1
        }
	] 
}, 200

mock_order = {
    "order_id": "ed854482-89a1-4423-aff6-91991a389e46",
    "summary": [
        {
            "cost": 0.5,
            "name": "orange",
            "quantity": 2
        },
        {
            "cost": 1.2,
            "name": "apple",
            "quantity": 4
        }
    ],
    "total": 1.7
}, 200

mock_summary = { 'summary': {}, 'total': 1.7 }, 200

mock_summary_db = [
    {
        'cost': 0.5,
        'name': 'orange',
        'quantity': 3
    }
]