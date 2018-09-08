import csv
import xml.etree.ElementTree as ET
from Airport import Airport


class Flight:
    def __init__(self, flight_number, airline, airport_from, airport_to):

        self.flight_number = flight_number
        self.airline = airline
        self.airport_from = airport_from
        self.airport_to = airport_to

        # Check that flight_number type is string
        if type(flight_number) is not str:
            raise TypeError("flight_number should be a string.")

        # Check that airline type is string
        if type(airline) is not str:
            raise TypeError("airline should be a string.")

        # Check that airport_from type is Airport
        if type(airport_from) is not Airport:
            raise TypeError("airport_from should be an instance of Airport class.")

        # Check that airport_to type is Airport
        if type(airport_to) is not Airport:
            raise TypeError("airport_to should be an instance of Airport class.")

    def __eq__(self, other):
        return (self.flight_number == other.flight_number and self.airline == other.airline and
                self.airport_from == other.airport_from and self.airport_to == other.airport_to)

    def __repr__(self):
        return "[Flight number: %s, Airline: %s, Origin: %s, Destination: %s]" % (self.flight_number,
                                                                                  self.airline,
                                                                                  repr(self.airport_from),
                                                                                  repr(self.airport_to))

    @staticmethod
    def get_flights_from_csv(csv_flights_file, airports_list, csv_header=False):
        """
        Reads csv_flights_file and returns list of flights.
        :param csv_flights_file: path to csv file
        :param airports_list: list of airport objects
        :param csv_header: Boolean, default value False (NO header in csv file). To use csv with header, use True.
        :return: list of airports in csv_flights_file
        """

        if csv_flights_file[-4:].lower() != '.csv':
            raise IOError("csv_flights_file should be .csv! ", csv_flights_file)

        for airport in airports_list:
            assert isinstance(airport, Airport)

        try:
            with open(csv_flights_file, 'r') as flights_csvfile:
                reader = csv.reader(flights_csvfile)
                csv_flights_list = []
                if csv_header:
                    next(reader)
                elif not csv_header:
                    pass
                else:
                    raise TypeError('csv_header should be Boolean! Provided csv_header = ', csv_header)
                for flight in reader:
                    if len(flight) != 4:
                        raise ValueError('Flight row should contain exactly 4 elements: Flight Number, Airline,'
                                         ' Airport From, Airport To', flight)
                    else:
                        csv_flight = Flight(flight[0], flight[1],
                                            Airport.find_airport_in_list(flight[2], airports_list),
                                            Airport.find_airport_in_list(flight[3], airports_list))
                        csv_flights_list.append(csv_flight)
                return csv_flights_list
        except IOError:
            raise IOError("Cannot open file", csv_flights_file)

    @staticmethod
    def get_flights_from_xml(xml_flights_file, airports_list):
        """
        Reads xml_flights_file and returns list of flights.
        Please see correct layout for xml in '.\\data\\flight.xsd'

        :param xml_flights_file: path to xml file
        :param airports_list: list of airport objects
        :return: list of airports in xml_flights_file
        """

        if xml_flights_file[-4:].lower() != '.xml':
            raise IOError("xml_flights_file should be .xml! ", xml_flights_file)

        for airport in airports_list:
            assert isinstance(airport, Airport)

        try:
            with open(xml_flights_file, 'r', encoding='utf-8') as s:
                tree = ET.parse(s)
                xml_flights_list = []
                for flight in tree.getroot().findall("flight"):
                    xml_flights = Flight(flight.attrib['number'], flight.find("airline").text,
                                         Airport.find_airport_in_list(flight.find("from").text, airports_list),
                                         Airport.find_airport_in_list(flight.find("to").text, airports_list))
                    xml_flights_list.append(xml_flights)
                return xml_flights_list
        except IOError:
            raise IOError("Cannot open file", xml_flights_file)


if __name__ == '__main__':
    airports_list_from_csv = Airport.get_airports_from_csv('.\\test_data\\airports.csv', csv_header=True)
    flights_list_from_csv = Flight.get_flights_from_csv('.\\test_data\\flights.csv',
                                                        airports_list_from_csv, csv_header=True)
    flights_list_from_xml = Flight.get_flights_from_xml('.\\test_data\\flights.xml',
                                                        airports_list_from_csv)

    print(flights_list_from_csv)
    print(flights_list_from_xml)
