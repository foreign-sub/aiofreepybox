class Contact:
    """
    Contact
    """

    def __init__(self, access):
        self._access = access

    add_to_group_schema = {"group_id": 1, "contact_id": 1}

    contact_object_type = ["numbers", "emails", "urls", "addresses"]

    group_schema = {"id": 0, "name": "", "nb_contact": 0}

    import_contacts_schema = {"empty_before_adding": False, "contacts": [""]}

    photo_url_schema = {"photo_url": ""}

    async def add_contact(self, contact_data):
        """
        Add contact

        contact_data : `dict`
        """
        return await self._access.post("contact/", contact_data)

    async def add_to_group(self, add_to_group):
        """
        Add to group

        add_to_group : `dict`
        """
        return await self._access.post("contact/addtogroup", add_to_group)

    async def create_contact_object(
        self, contact_id, contact_data, contact_object_type
    ):
        """
        Create contact object

        contact_id : `int`
        contact_data : `dict`
        contact_object_type : `str`
        """
        return await self._access.post(
            f"contact/{contact_id}/{contact_object_type}", contact_data
        )

    async def create_group(self, group_data):
        """
        Create group

        group_data : `dict`
        """
        return await self._access.post("group/", group_data)

    async def delete_contact_object(self, contact_id, contact_object_type):
        """
        Delete contact object

        contact_id : `int`
        contact_object_type : `str`
        """
        await self._access.delete(f"contact/{contact_id}/{contact_object_type}")

    async def delete_group(self, group_id):
        """
        Delete group

        group_id : `int`
        """
        await self._access.delete(f"group/{group_id}")

    async def edit_contact_object(self, contact_id, contact_data, contact_object_type):
        """
        Edit contact object

        contact_id : `int`
        contact_data : `dict`
        contact_object_type : `str`
        """
        return await self._access.put(
            f"contact/{contact_id}/{contact_object_type}", contact_data
        )

    async def export_contacts(self):
        """
        Export contacts to vcf format
        """
        return await self._access.post("contact/export/")

    async def get_contact(self, contact_id):
        """
        Get contact

        contact_id : `int`
        """
        return await self._access.get(f"contact/{contact_id}")

    async def get_contact_data(self, contact_id, contact_object_type):
        """
        Get contact data

        contact_id : `int`
        contact_object_type : `str`
        """
        return await self._access.get(f"contact/{contact_id}/{contact_object_type}")

    async def get_contacts(self):
        """
        Get contacts
        """
        return await self._access.get("contact/")

    async def get_contacts_count(self):
        """
        Get contacts count
        """
        return await self._access.get("contact/count")

    async def get_contact_groups(self):
        """
        Get contacts groups
        """
        return await self._access.get("contact/groups")

    async def get_group(self, group_id):
        """
        Get group

        group_id : `int`
        """
        return await self._access.get(f"group/{group_id}")

    async def get_groups(self):
        """
        Get groups
        """
        return await self._access.get("group/?page=1&start=0&limit=200")

    async def import_contacts_step1(self, import_contacts_vcard):
        """
        Import contacts step 1

        import_contacts_vcard : `dict`
        """
        return await self._access.post("contact/import/step1/", import_contacts_vcard)

    async def import_contacts_step2(self, import_contacts):
        """
        Import contacts step 2

        import_contacts : `dict`
        """
        return await self._access.post("contact/import/step2/", import_contacts)

    async def remove_from_group(self, remove_from_group):
        """
        Remove from group

        remove_from_group : `dict`
        """
        return await self._access.post("contact/removefromgroup", remove_from_group)

    async def update_contact(self, contact_id, contact_data):
        """
        Update contact

        contact_id : `int`
        contact_data : `dict`
        """
        return await self._access.put(f"contact/{contact_id}", contact_data)

    async def update_contact_photo(self, contact_id, photo_url):
        """
        Update contact photo

        contact_id : `int`
        photo_url : `dict`
        """
        return await self._access.put(f"contact/{contact_id}/update_photo/", photo_url)
