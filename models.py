from dataclasses import dataclass


@dataclass
class Master:
    master_id: int
    name: str


@dataclass
class Service:
    service_id: int
    name: str


@dataclass
class Appoinment:
    id: int
    client_name: str
    master_id: int
    service_id: int
    time: str
