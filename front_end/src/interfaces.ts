export interface IDomains {
    [key: string]: [string] | [];
}
export interface IConnections {
    [index: number]: {
        resourceName: string;
        etag: string;
        emailAddresses?: {
            [index: number]: {
                value: string;
            };
        };
    };
    [Symbol.iterator](): any;
}
export interface IJsonResponse {
    nextPageToken: string | undefined;
    connections: IConnections;
}