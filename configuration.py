CONTRACT_ADDRESS = "0xA69fC8DEa8e2289fDfC0f14611942C4FD54B4E55"
ABI = """
[
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "address",
				"name": "_to",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "_amount",
				"type": "uint256"
			}
		],
		"name": "TX",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "address",
				"name": "_ownerAddress",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "_estateId",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "_adId",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "_date",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "_cost",
				"type": "uint256"
			}
		],
		"name": "adCreated",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_buyer",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_cost",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "_estateId",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_date",
				"type": "string"
			},
			{
				"internalType": "bool",
				"name": "_open",
				"type": "bool"
			},
			{
				"internalType": "uint256",
				"name": "_adId",
				"type": "uint256"
			}
		],
		"name": "addAD",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_area",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_estateaddress",
				"type": "string"
			},
			{
				"internalType": "enum MyShop.Type",
				"name": "_estatetype",
				"type": "uint8"
			},
			{
				"internalType": "bool",
				"name": "_active",
				"type": "bool"
			},
			{
				"internalType": "uint256",
				"name": "_estateId",
				"type": "uint256"
			}
		],
		"name": "addEstate",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_userAddress",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_balance",
				"type": "uint256"
			}
		],
		"name": "addUser",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_adId",
				"type": "uint256"
			}
		],
		"name": "adStatus",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "address",
				"name": "_ownerAddress",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "_estateId",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "_date",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "bool",
				"name": "_active",
				"type": "bool"
			}
		],
		"name": "adStatusChanged",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_estateId",
				"type": "uint256"
			}
		],
		"name": "eastateStatus",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "address",
				"name": "_ownerAddress",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "_estateId",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "enum MyShop.Type",
				"name": "_typeEstate",
				"type": "uint8"
			}
		],
		"name": "estateCreated",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "address",
				"name": "_ownerAddress",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "address",
				"name": "_buyerAddress",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "_estateId",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "_adId",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "bool",
				"name": "_open",
				"type": "bool"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "_date",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "_cost",
				"type": "uint256"
			}
		],
		"name": "estatePurchased",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "address",
				"name": "_ownerAddress",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "_estateId",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "_adId",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "_date",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "bool",
				"name": "_open",
				"type": "bool"
			}
		],
		"name": "estateStatusChanged",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "address",
				"name": "_to",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "_amount",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "_date",
				"type": "string"
			}
		],
		"name": "fundsBack",
		"type": "event"
	},
	{
		"inputs": [],
		"name": "replenishment",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_amount",
				"type": "uint256"
			}
		],
		"name": "replenishmentTwo",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_adId",
				"type": "uint256"
			}
		],
		"name": "SellEstate",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "withdrawall",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_amount",
				"type": "uint256"
			}
		],
		"name": "withdrawallTwo",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "ADs",
		"outputs": [
			{
				"internalType": "address",
				"name": "seller",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "buyer",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "cost",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "estateId",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "date",
				"type": "string"
			},
			{
				"internalType": "bool",
				"name": "open",
				"type": "bool"
			},
			{
				"internalType": "uint256",
				"name": "adId",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "estates",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "area",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "estateadress",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"internalType": "enum MyShop.Type",
				"name": "estateType",
				"type": "uint8"
			},
			{
				"internalType": "bool",
				"name": "active",
				"type": "bool"
			},
			{
				"internalType": "uint256",
				"name": "estateId",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getAd",
		"outputs": [
			{
				"components": [
					{
						"internalType": "address",
						"name": "seller",
						"type": "address"
					},
					{
						"internalType": "address",
						"name": "buyer",
						"type": "address"
					},
					{
						"internalType": "uint256",
						"name": "cost",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "estateId",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "date",
						"type": "string"
					},
					{
						"internalType": "bool",
						"name": "open",
						"type": "bool"
					},
					{
						"internalType": "uint256",
						"name": "adId",
						"type": "uint256"
					}
				],
				"internalType": "struct MyShop.AD[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getBalance",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getEstate",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "area",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "estateadress",
						"type": "string"
					},
					{
						"internalType": "address",
						"name": "owner",
						"type": "address"
					},
					{
						"internalType": "enum MyShop.Type",
						"name": "estateType",
						"type": "uint8"
					},
					{
						"internalType": "bool",
						"name": "active",
						"type": "bool"
					},
					{
						"internalType": "uint256",
						"name": "estateId",
						"type": "uint256"
					}
				],
				"internalType": "struct MyShop.Estate[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
"""