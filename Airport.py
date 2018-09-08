import csv


class AirportLogicError(Exception):
    """Basic class for custom Airport exceptions"""
    pass


class BothIcaoIataNoneError(AirportLogicError):
    """Exception raised if both IATA and ICAO codes are missing. At least one of them must be defined."""
    pass


class Airport:
    name = None
    iata = None
    icao = None

    def __init__(self, name, iata=None, icao=None):

        if (not icao) & (not iata):
            raise BothIcaoIataNoneError("Both IATA and ICAO codes are None for %s. Define at least one of them" % name)

        # Check that Name type is string
        if type(name) is not str:
            raise TypeError("Airport name must be a string.")

        # Check IATA code length
        if iata:  # iata is not None or empty
            if len(iata) != 3:
                raise ValueError('IATA length must be 3 symbols! \n iata = ', iata)

        # Check ICAO code length
        if icao:  # icao is not None or empty
            if len(icao) != 4:
                raise ValueError("ICAO length must be 4 symbols! \n icao = ", icao)

        self.name = name
        self.iata = iata
        self.icao = icao

    def __eq__(self, other):
        return self.name == other.name and self.iata == other.iata and self.icao == other.icao

    def __repr__(self):
        return "[%s, %s, %s]" % (self.name, self.iata, self.icao)

    @staticmethod
    def find_airport_in_list(airport_field, airports_list_to_find):

        """
        This method finds airport by airport_field in airports_list_to_find
        If no airport is found, raises RuntimeError.

        :param airport_field : any of airport fields (name or iata or icao)
        :param airports_list_to_find : list of airports to look in
        :return: airport object or None if no airport in list matches
        """

        if not airport_field:
            raise ValueError("Airport field can not be empty!")

        for airport in airports_list_to_find:

            if airport.name == airport_field or airport.iata == airport_field or airport.icao == airport_field:
                return airport
        # if we are here, no airport is found
        return None

    @staticmethod
    def get_airports_from_csv(airports_filename, csv_header=False):

        """
        Reads csv file and returns list of airport objects from it.

        :param airports_filename: path to csv file with airports
        :param csv_header: Boolean, default value False (NO header in csv file). To use csv with header, use True.
        :return: list of airports from csv file
        """

        if airports_filename[-4:].lower() != '.csv':
            raise IOError("Airport filename must be .csv! ", airports_filename)

        try:
            with open(airports_filename, 'r') as airports_csv:
                reader = csv.reader(airports_csv)
                airports_list_from_csv = []
                if csv_header:  # if csv_header is true
                    next(reader)
                for airport_item in reader:
                    # print(airport_item)
                    if len(airport_item) != 3:
                        raise ValueError('Airport row should  contain exactly 3 elements: Name, IATA, ICAO!!! Wrong '
                                         'for line: ', airport_item)
                    else:
                        airport = Airport(airport_item[0], airport_item[1], airport_item[2])
                        airports_list_from_csv.append(airport)
                return airports_list_from_csv
        except IOError:
            raise IOError("Cannot open file", airports_filename)


if __name__ == '__main__':
    airports_list = Airport.get_airports_from_csv('.\\test_data\\airports.csv', csv_header=True)
    print(airports_list)
