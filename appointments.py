from datetime import datetime, time as clock_time

from models import Appoinment, Master, Service


masters = [Master(1, "Анна"), Master(2, "Мария")]
services = [Service(1, "Стрижка")]
appointments: list[Appoinment] = []


def get_master(master_id: int) -> Master | None:
    return next((master for master in masters if master.master_id == master_id), None)


def get_service(service_id: int) -> Service | None:
    return next((service for service in services if service.service_id == service_id), None)


def create_appointment(
    client_name: str,
    master_id: int,
    service_id: int,
    time: str,
) -> Appoinment | None:
    if not isinstance(client_name, str) or not client_name.strip():
        return None
    if not master_id or not service_id or not isinstance(time, str):
        return None

    master = get_master(master_id)
    service = get_service(service_id)
    if master is None or service is None:
        return None

    try:
        appointment_time = datetime.strptime(time, "%H:%M").time()
    except ValueError:
        return None

    if appointment_time.strftime("%H:%M") != time:
        return None
    if not clock_time(8, 0) <= appointment_time <= clock_time(20, 0):
        return None

    if any(
        appointment.master_id == master.master_id and appointment.time == time
        for appointment in appointments
    ):
        return None

    appointment = Appoinment(
        id=max((item.id for item in appointments), default=0) + 1,
        client_name=client_name.strip(),
        master_id=master.master_id,
        service_id=service.service_id,
        time=time,
    )
    appointments.append(appointment)
    return appointment
