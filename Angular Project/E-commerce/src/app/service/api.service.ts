import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import {catchError, map, retry, timeout} from 'rxjs/operators';
@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private httpClient;
  private baseURL = environment.BASE_URL;

  constructor(http: HttpClient) {
    this.httpClient = http;
  }


  /* this function is used to build the query parameter 
    using the objects like url?key1=val1&key2=val2&key3=val3*/
  private buildQueryParams(paramsObject: any): string {
    try {
      let queryParams = '';
      console.log(paramsObject);
      if (paramsObject != null) {
        for (const key in paramsObject) {
          console.log(queryParams);
          if (queryParams === '') {
            queryParams = '?' + key + '=' + paramsObject[key];
          } else {
            queryParams = queryParams +  '&' + key + '=' + paramsObject[key];
          }
        }
      }
      return queryParams;
    }
    catch (e) {
      throw e;
    }
  }
   
  /* This function is used to call the web server to get the
   data by passing query parameter and the url which returns
   json object or json array*/


  getData(url:any, params:any) : Observable<any> {
    let queryParam  = this.buildQueryParams(params) ;
    var data = null ;
    try {
      return this.httpClient.get(this.baseURL + url + queryParam).pipe(
        map(response => {
          let a:any = response;
          if (a['response_object'] === undefined) {
            data = response;
          } else {
            data = a['response_object'];
          }
          return data;
        }),
        catchError(ex => {
          return ex;
        })
      );
    } catch (e) {
      throw(e);
    }
   }

  postData(url:any, json_key:string,  param:any) : Observable<any> {
    var formDAtaObject: any = new FormData();
    formDAtaObject.append(json_key, JSON.stringify(param));

    try {
      return this.httpClient.post(this.baseURL + url, formDAtaObject).pipe(
        map(response => {
        
          return response;
        }),
        catchError(ex => {
          return ex;
        })
      );
    } catch (e) {
      throw(e);
    }
   
  }
  
}
